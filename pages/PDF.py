import streamlit as st
from fpdf import FPDF
import base64
from datetime import datetime
from pages import Ficha

def pdf():
    # Crie uma instância da classe FPDF e defina as propriedades básicas
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Adicione algum conteúdo ao PDF
    pdf.cell(200, 10, txt=f"{Ficha.resultado.head().iat[0, 0]} Olá, mundo!", ln=True, align='C')

    # Salve o PDF em uma variável
    pdf_output = pdf.output(dest='S').encode('latin1')

    # Codifique o PDF para base64
    b64 = base64.b64encode(pdf_output)
    b64 = b64.decode()

    # Crie um link de download para o PDF
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="meu_arquivo.pdf">Clique aqui para baixar o PDF</a>'
    st.markdown(href, unsafe_allow_html=True)