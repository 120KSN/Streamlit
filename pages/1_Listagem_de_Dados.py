import streamlit as st
from Inicio import dados

# título da página (H1)
st.title("Página de Listagem de Dados")
# texto mostrado na página
st.write("Esta é a primeira subpágina que existe no sistema.")

# título de menor nível (H2)
st.subheader("Exemplos de dados")

# os dados são exibidos em um "dataframe"
st.dataframe(dados)

# se clicar em um botão chamado "Voltar ao início"...
if st.button("Voltar ao início"):
    # retorna à página inicial
    st.switch_page("Inicio.py")