# aula 1 - intro pandas
import pandas as pd
import numpy as np

series = pd.Series([10, 20, 30, 40])

print(series)

data = {'Nome': ['Ana', 'João', 'Maria'], 'Idade': [20, 32, 44]}

df = pd.DataFrame(data)

print(df)

print(df.info())

print(df.describe())

# aula 2 - criação de dataframes

df = pd.DataFrame([[1, 'A'], [2, 'B'], [3, 'C']], columns=['ID', 'Letra'])

print(df)

array = np.array([[10, 20], [30, 40]])

df = pd.DataFrame(array, columns=['Col1', 'Col2'])

print(df)

df = pd.read_csv("manip_de_dados/dados.csv")

print(df)

df = pd.read_csv('manip_de_dados/teste.csv')

df = df.fillna("Valor Padrão").infer_objects(copy=False)

print(df)

# aula 3- manipulação com pandas

df['Está Empregado'] = [False, False, True, True, False]

print(df)

df = df.drop(columns=["Idade"])

print(df)

# Converte a coluna para numérico (transforma valores inválidos em NaN)
df['Salário'] = pd.to_numeric(df['Salário'], errors='coerce')

# Preenche os NaN com 0 (ou outro valor padrão se preferir)
df['Salário'] = df['Salário'].fillna(0)

# Agora a soma funciona
df['Salário'] = df['Salário'] + 100

print(df)

# Cria a coluna de categoria
df['Categoria'] = df['Salário'].apply(lambda x: 'Ganha bem' if x > 4000 else 'Ganha mal')

print(df)

# aula 4 - valores ausentes

df = pd.DataFrame({'A': [1, None, 3], 'B': [1, 5, None], 'C': [6, None, None]})

print(df.isnull())

df_sem_nulos = df.dropna()

print(df_sem_nulos)

df_preenchido = df.fillna(0).infer_objects(copy=False)

print(df_preenchido)

df_ffill = df.ffill().infer_objects(copy=False)

print(df_ffill)
