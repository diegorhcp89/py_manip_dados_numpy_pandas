import pandas as pd

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
