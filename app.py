import streamlit as st

st.title("Especializaciòn Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Fabricio Huanuco")

valor_inicial = st.number_input("Ingrese el valor inicial")
valor_final = st.number_input("Ingrese el valor final")

lista_numeros = list(range(int(valor_inicial), int(valor_final)))
st.write(lista_numeros)
