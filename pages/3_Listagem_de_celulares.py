import streamlit as st

dados = {
    "Número": [],
    "Marca": [],
    "Modelo": [],
    "Operadora": []
}

# título da página (H1)
st.title("Página de Listagem de Celulares")
# texto mostrado na página
st.write("Esta é a terceira subpágina que existe no sistema.")

numero = st.text_input("Digite o número do celular:")
marca = st.text_input("Digite a marca do celular:")
modelo = st.text_input("Digite o modelo do celular:")
operadora = st.text_input("Digite a operadora do celular:")

# se clicar no botão "Enviar"
if st.button("Enviar"):
    # se foi preenchido o nome
    if numero and marca and modelo and operadora:
        dados["Número"].append(numero)
        dados["Marca"].append(marca)
        dados["Modelo"].append(modelo)
        dados["Operadora"].append(operadora)

        st.success("Dados salvos com sucesso.")
    else:
        st.warning("Por favor, digite seu nome.")

# título de menor nível (H2)
st.subheader("Exemplos de dados")

# os dados são exibidos em um "dataframe"
st.dataframe(dados)

# se clicar em um botão chamado "Voltar ao início"...
if st.button("Voltar ao início"):
    # retorna à página inicial
    st.switch_page("Inicio.py")