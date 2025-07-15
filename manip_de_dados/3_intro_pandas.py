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
