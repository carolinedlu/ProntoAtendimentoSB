import streamlit as st
import csv
import time

st.title('Cadastros')


def save_name(nomecompleto, nomemae, numerocartao, cpf, rg, datanascimento, sexo, telefone, endereco, cep, municipio, estado, atendente):
    filename = 'db2.csv'
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nomecompleto, nomemae, numerocartao, cpf, rg, datanascimento, sexo, telefone, endereco, cep, municipio, estado, atendente])
    delay = 5
    start_time = time.time()
    st.markdown('Cadastro efetuado')
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= delay:
            st._rerun()
            break


nomecompleto = st.text_input('Nome completo:')
nomemae = st.text_input('Nome da mãe:')
numerocartao = st.text_input('Numero do cartão:')
cpf = st.text_input('CPF')
rg = st.text_input('RG')
datanascimento = st.date_input('Data de Nascimento')
sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
telefone = st.text_input('Telefone')
endereco = st.text_input('Endereço completo')
cep = st.text_input('CEP')
municipio = st.text_input('Município')
estado = st.text_input('Estado')
atendente = st.text_input('Nome do Atendente')
if st.button('Salvar'):
    save_name(nomecompleto, nomemae, numerocartao, cpf, rg, datanascimento, sexo, telefone, endereco, cep, municipio, estado, atendente)
