"""
Mini Analisador de Vendas em Python
Autor: Renato Brilhante
Descrição:
Este script cria um dataset fictício de vendas,
gera estatísticas descritivas, identifica o produto mais vendido
e exibe um gráfico de barras para visualização.

Bibliotecas necessárias:
- pandas
- matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# Criando um dataset fictício de vendas
data = {
    "Produto": ["Notebook", "Smartphone", "Headset", "Monitor", "Teclado", "Mouse"],
    "Vendas": [150, 300, 120, 90, 200, 250],
    "Preço Médio": [3500, 1800, 250, 1200, 150, 100]
}

df = pd.DataFrame(data)

# Exibindo estatísticas básicas
print("📊 Estatísticas das Vendas:")
print(df.describe())

# Produto mais vendido
mais_vendido = df.loc[df["Vendas"].idxmax()]
print(f"\n🔥 Produto mais vendido: {mais_vendido['Produto']} ({mais_vendido['Vendas']} unidades)")

# Gráfico de vendas
plt.figure(figsize=(8,5))
plt.bar(df["Produto"], df["Vendas"], color="royalblue")
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.show()
