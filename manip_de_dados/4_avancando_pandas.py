import pandas as pd
from sqlalchemy import create_engine

# aula 1 - filtragem

data = {'Nome': ['Ana', "João", "Maria"], 'Idade': [20, 32, 44]}

df = pd.DataFrame(data)

filtro_idade = df['Idade'] >= 30

print(filtro_idade)

print(df[filtro_idade])

print(df['Nome'])

filtro_por_condicao = (df['Idade'] >= 20) & (df['Nome'] == 'Ana')

print(df[filtro_por_condicao])

print(df.query("Idade > 40 and Nome != 'Francisco'"))

# aula 2 - operacoes estatisticas

df = pd.DataFrame({'Categoria': ['A', 'A', 'B'], 'Valor': [10, 20, 30]})

print(df.describe())

print(df['Valor'].mean())

print(df['Valor'].sum())

grupo = df.groupby('Categoria')

print(grupo.sum())

print(grupo.agg({'Valor': ['mean', 'max']}))

print(grupo['Valor'].count())

# aula 3 - lendo diferentes tipos de dados

try:
    df = pd.read_csv("manip_de_dados/dados.csv")
    print(df.head())
except FileNotFoundError:
    print("Erro ao ler dados.csv")

try:
    df_excel = pd.read_excel('manip_de_dados/dados.xlsx')
    print(df_excel.head())
except FileNotFoundError:
    print("erro ao ler dados.xlsx")

try:
    df_jason = pd.read_json('manip_de_dados/dados.json')
    print(df_jason.head())
except FileNotFoundError:
    print('erro ao ler dados.json')

engine = create_engine("sqlite:///manip_de_dados/dados.dados.db")

data = {
    'ID': [1, 2, 3],
    'Nome': ['Ana', 'João', 'Paulo'],
    'Idade': [20, 30, 40],
    'Cidade': ['São Paulo', 'Floripa', 'Rio de Janeiro']
}

pd.DataFrame(data).to_sql('tabela', con=engine, if_exists='replace', index=False)

try:
    df_sql = pd.read_sql('SELECT * FROM tabela', con=engine)
    print(df_sql.head())
except Exception as e:
    print(e)
