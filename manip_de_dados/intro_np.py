import numpy as np
import pandas as pd

dados = [1, 2, 3, 4, 5]

dados_quadrados = [x**2 for x in dados]

print(dados_quadrados)

dados_np = np.array([1, 2, 3, 4, 5])

dados_quadrados_np = dados_np ** 2

print(dados_quadrados_np)

dados = pd.read_csv("manip_de_dados/dados.csv")

print(dados.head())

dados["coluna_existente"] = dados["coluna_existente"] * 2

print(dados.head())
