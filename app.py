import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora",
    page_icon="🧮",
)

# Título da página
st.title("Calculadora Simples")

# Entrada de dados
num1 = st.number_input("Digite o primeiro número:", step=1.0)
num2 = st.number_input("Digite o segundo número:", step=1.0)

# Seleção da operação
operacao = st.selectbox("Selecione a operação", ("Soma", "Subtração", "Multiplicação", "Divisão"))

# Lógica para calcular o resultado
if operacao == "Soma":
    resultado = num1 + num2
elif operacao == "Subtração":
    resultado = num1 - num2
elif operacao == "Multiplicação":
    resultado = num1 * num2
elif operacao == "Divisão":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."

# Exibição do resultado
if st.button("Calcular"):
    st.write(f"Resultado: {resultado}")
