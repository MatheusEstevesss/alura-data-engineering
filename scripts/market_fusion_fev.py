from process_data import Data

# Extract data

path_companyA = r'data_raw/dados_empresaA.json'
path_companyB = r'data_raw/dados_empresaB.csv'

data_companyA = Data(path_companyA, 'json')
data_companyB = Data(path_companyB, 'csv')

# TRANSFORMING DATA

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

data_companyB.rename_columns(key_mapping)

matching_data = Data.matching_data(data_companyA, data_companyB)

# Load data

path = 'data_processed/matching_data_refactor_2.csv'

print(matching_data.saving_data(path))