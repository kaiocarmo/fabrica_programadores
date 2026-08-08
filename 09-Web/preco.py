# Autor: Kaio Carmo Siqueira
# Projeto: Minha primeira página web

# importando a biblioteca
import streamlit as st

st.write('--- Seja Bem Vindo ao Mercado Carmo Promos!!! ---')
st.text_input('Banana ')
st.text_input('Custo de mão de obra')
st.text_input('Custo de energia')
st.text_input('Custo de internet')
st.text_input('Custo de Água')
st.button('Calcular preço de venda')