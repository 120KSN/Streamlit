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
marca = st.selectbox("Selecione a marca do seu celular:", options= ["Samsung","Apple","Xiaomi","Vivo","Oppo","Realme","Motorola","Google","OnePlus","Huawei",])
modelo = st.text_input("Digite o modelo do celular:")
operadora = st.selectbox("Selecione a operadora do seu celular:", options= ["Vivo","Claro","TIM","Algar Telecom","Arqia","Surf Telecom","Telecall","NLT","Brisanet","Vero"])

# se clicar no botão "Enviar"
if st.button("Enviar"):
    # se foi preenchido o nome
    if numero and not (len(numero) > 13 or len(numero) < 13 or numero[2] != " " or numero[8] != "-"):
        if marca:
            if modelo:
                if operadora:
                    dados["Número"].append(numero)
                    dados["Marca"].append(marca)
                    dados["Modelo"].append(modelo)
                    dados["Operadora"].append(operadora)

                    st.success("Dados salvos com sucesso.")
                else:
                    st.warning("Por favor, selecione sua operadora")
            else:
                st.warning("Por favor, digite o modelo do seu celular")
        else:
            st.warning("Por favor selecione sua marca")
            
    elif len(numero) > 13 or len(numero) < 13 or numero[2] != " " or numero[8] != "-":
        st.warning("O número deve estar no formato: XX XXXXX-XXXX")
    else:
        st.warning("Por favor, digite seu número")

# título de menor nível (H2)
st.subheader("Exemplos de dados")

# os dados são exibidos em um "dataframe"
st.dataframe(dados)

# se clicar em um botão chamado "Voltar ao início"...
if st.button("Voltar ao início"):
    # retorna à página inicial
    st.switch_page("Inicio.py")