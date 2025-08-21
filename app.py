"""
Dashboard de Análise de Vendas
Autor: Renato Brilhante

Descrição:
Este dashboard interativo em Streamlit permite explorar
dados de vendas, gerando métricas de negócio e visualizações.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# 1. Carregar os dados
# =============================
st.title("📊 Dashboard de Análise de Vendas")
df = pd.read_csv("vendas.csv")

# =============================
# 2. Criar colunas calculadas
# =============================
df["Receita"] = df["Quantidade"] * df["Preco"]

# =============================
# 3. Métricas principais
# =============================
receita_total = df["Receita"].sum()
ticket_medio = df["Receita"].mean()
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Receita Total", f"R$ {receita_total:,.2f}")
col2.metric("📦 Ticket Médio", f"R$ {ticket_medio:,.2f}")
col3.metric("🔥 Produto Mais Vendido", produto_mais_vendido)

# =============================
# 4. Vendas por produto
# =============================
st.subheader("📦 Quantidade Vendida por Produto")
vendas_por_produto = df.groupby("Produto")["Quantidade"].sum()

fig1, ax1 = plt.subplots(figsize=(7,4))
vendas_por_produto.plot(kind="bar", color="royalblue", ax=ax1)
ax1.set_xlabel("Produto")
ax1.set_ylabel("Unidades Vendidas")
st.pyplot(fig1)

# =============================
# 5. Receita por produto
# =============================
st.subheader("💵 Participação na Receita por Produto")
receita_por_produto = df.groupby("Produto")["Receita"].sum()

fig2, ax2 = plt.subplots(figsize=(6,6))
receita_por_produto.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colormap="tab20",
    ax=ax2
)
ax2.set_ylabel("")
st.pyplot(fig2)

# =============================
# 6. Exibir tabela de dados
# =============================
st.subheader("📄 Dados Originais")
st.dataframe(df)
