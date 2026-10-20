import streamlit as st
from Inicio import dados
import random

st.title("Página de Solicitação de Nome")
st.write("Esta é a segunda subpágina.")

nome = st.text_input("Digite seu nome:")
idade = st.text_input("Digite sua idade:")

# se clicar no botão "Enviar"
if st.button("Enviar"):
    # se foi preenchido o nome
    if nome and idade:
        try:
            idade = int(idade)
            st.success(f"Olá, {nome}! Seja bem-vindo.")
            dados["Nome"].append(nome)
            dados["Idade"].append(idade)
        except:
            st.warning("Idade deve ser um número")
    else:
        st.warning("Por favor, digite seu nome.")

# se clicar no botão de "Voltar"...
if st.button("Voltar ao início"):
    # "vai" para a página inicial
    st.switch_page("Inicio.py")
