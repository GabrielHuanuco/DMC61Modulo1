import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Fabricio Huanuco")
st.image("Python_logo.png", width = 200)

modulos = st.sidebar.selectbox("Seleccione un modulo", ["Modulo Listas","Modulo Arreglos","Modulo Funciones"])
if modulos == "Modulo Listas":
  st.write("Bienvenido al módulo Listas")
  valor_inicial = st.number_input("Ingrese el valor inicial")
  valor_final = st.number_input("Ingrese el valor final")
  lista_numeros = list(range(int(valor_inicial), int(valor_final)))
  st.write(lista_numeros)
elif modulos == "Modulo Arreglos":
  st.write("Bienvenido al módulo de Arreglos")
else:
  st.write("Bienvenido al módulo de Funciones")
