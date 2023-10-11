import streamlit as st
import pandas as pd
from Controller import controller as controler
# Carregue o arquivo CSV
df = pd.read_csv('db2.csv')

# Solicite ao usuário que insira o nome para pesquisa
nome = st.selectbox('Selecione um nome:', controler.df().drop_duplicates(["nomecompleto"]))

# Filtrar o dataframe com base no nome
df_filtrado = df[df['nomecompleto'] == nome]  # substitua 'nome' pelo nome da coluna que contém os nomes

# Exiba o dataframe filtrado no editor de dados
df_filtrado = st.dataframe(df_filtrado).data_editor(df_filtrado)

# Salve as alterações de volta para o arquivo CSV
if st.button('Salvar alterações'):
    df.update(df_filtrado)
    df.to_csv('db2.csv', index=False)