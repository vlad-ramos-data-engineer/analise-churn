'''Ingestão e limpeza da base de clientes para análise de churn.

Lê o CSV bruto, converte a coluna de data de cadastro para datetime
(marcando datas inválidas como nulas em vez de quebrar o pipeline) e
reporta a qualidade dos dados carregados.
'''
from pathlib import Path

import pandas as pd

CAMINHO_DADOS = Path('data/clientes_churn.csv')


def carregar_dados(caminho: Path = CAMINHO_DADOS) -> pd.DataFrame:
    '''Carrega o CSV e converte `data_cadastro` para datetime.

    Datas em formatos inconsistentes ou impossíveis (ex.: `2024-02-30`,
    `data_invalida`) são convertidas para NaT (nulo) com `errors='coerce'`,
    preservando a linha para não perder o cliente na análise.
    '''
    clientes = pd.read_csv(caminho)
    clientes['data_cadastro'] = pd.to_datetime(
        clientes['data_cadastro'], errors='coerce', format='mixed'
    )
    return clientes


def relatorio_qualidade(clientes: pd.DataFrame) -> None:
    '''Imprime um resumo da qualidade dos dados carregados.'''
    total = len(clientes)
    datas_invalidas = int(clientes['data_cadastro'].isna().sum())
    percent = datas_invalidas / total * 100

    print(clientes.head(10))
    print()
    print(f'Base carregada: {total} linhas e {clientes.shape[1]} colunas.')
    print(
        f'{datas_invalidas} linhas ({percent:.2f}%) têm data de cadastro '
        'inválida ou ausente — investigar o contrato de dados junto à origem.'
    )


if __name__ == '__main__':
    relatorio_qualidade(carregar_dados())
