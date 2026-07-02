import pandas as pd

churn = pd.read_csv('data/clientes_churn.csv')

def calcular_churn_plano(tabela):
    resultado = tabela.groupby('plano').agg(
        n_clientes=('churn','size'),n_nulos=('churn', 'count'), taxa_churn_percent=('churn', 'mean'))
    resultado['taxa_churn_percent'] = resultado["taxa_churn_percent"] * 100
    return resultado

resultado = calcular_churn_plano(churn)
assert len(churn) == churn['churn'].count()
print(resultado)