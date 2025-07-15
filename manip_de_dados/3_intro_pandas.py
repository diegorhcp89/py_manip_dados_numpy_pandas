# aula 1 - intro pandas
import pandas as pd

series = pd.Series([10, 20, 30, 40])

print(series)

data = {'Nome': ['Ana', 'João', 'Maria'], 'Idade': [20, 32, 44]}

df = pd.DataFrame(data)

print(df)

print(df.info())

print(df.describe())
