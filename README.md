# Análise de Churn

Pipeline simples de leitura e análise de churn de clientes em Python.

## Stack

- Python 3
- Pandas

## Estrutura

```
.
├── README.md
├── .gitignore
├── ingestao.py         # Lê o CSV e faz limpeza de datas
├── analise_churn.py    # Calcula taxa de churn por plano
└── data/               # Dados brutos (não versionado)
```

## Como rodar

```bash
git clone https://github.com/vlad-ramos-data-engineer/analise-churn.git
cd analise-churn
pip install pandas
python3 ingestao.py
python3 analise_churn.py
```

## Dados

Base fictícia de 150 clientes com colunas: `cliente_id`, `nome`, `data_cadastro`, `plano`, `mrr`, `churn`. O arquivo `data/clientes_churn.csv` não está versionado (protegido por `.gitignore`).

## Autor

Vlad — estudando engenharia de dados.