'''Cálculo da taxa de churn por plano.

Consome a base já limpa por `ingestao.carregar_dados` e agrega churn por
plano. Inclui um alerta de negócio para segmentos com amostra pequena,
cuja taxa de churn é estatisticamente instável.
'''
import pandas as pd

from ingestao import carregar_dados

# Abaixo desse tamanho a taxa de churn de um segmento é volátil (n < 30):
# um único cliente muda muito o percentual. Regra prática de estatística.
AMOSTRA_MINIMA = 30


def calcular_churn_plano(tabela: pd.DataFrame) -> pd.DataFrame:
    '''Agrega churn por plano.

    Retorna, por plano: total de clientes, registros não-nulos de churn
    (o `.count()` do pandas conta os NÃO-nulos), total de clientes que
    deram churn e a taxa de churn em %.
    '''
    resultado = tabela.groupby('plano').agg(
        n_clientes=('churn', 'size'),
        nao_nulos=('churn', 'count'),
        total_churn=('churn', 'sum'),
        taxa_churn_percent=('churn', 'mean'),
    )
    resultado['taxa_churn_percent'] = resultado['taxa_churn_percent'] * 100
    return resultado


def alertas_amostra(resultado: pd.DataFrame) -> list[str]:
    '''Gera alertas de negócio para planos com amostra pequena (n < 30).'''
    pequenos = resultado[resultado['n_clientes'] < AMOSTRA_MINIMA]
    alertas = []
    for plano, linha in pequenos.iterrows():
        alertas.append(
            f'ATENÇÃO: o plano {plano} tem apenas {int(linha["n_clientes"])} '
            f'clientes (amostra < {AMOSTRA_MINIMA}). Sua taxa de churn de '
            f'{linha["taxa_churn_percent"]:.1f}% é volátil — cada cliente pesa '
            'muito no percentual. Trate como indício, não como base para '
            'decisão isolada, e colete mais dados antes de agir.'
        )
    return alertas


if __name__ == '__main__':
    resultado = calcular_churn_plano(carregar_dados())
    print(resultado)
    print()
    for alerta in alertas_amostra(resultado):
        print(alerta)
