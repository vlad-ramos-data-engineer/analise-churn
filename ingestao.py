import pandas as pd

clientes = pd.read_csv( "data/clientes_churn.csv" )
clientes['data_cadastro'] = pd.to_datetime(clientes['data_cadastro'], errors='coerce', format='mixed')
data_out = clientes['data_cadastro'].isna().sum()

amostra = clientes.head(10)
percent = (data_out / clientes.shape[0] ) * 100

print(amostra)
print(f"Arquivo importado e analisado: possui {clientes.shape[0]} linhas e {clientes.shape[1]} colunas")
print(f"E em {data_out} linhas os dados de data estão inválidos, correspondendo à {percent:.2f}% das linhas - investigar contrato junto à source") 


