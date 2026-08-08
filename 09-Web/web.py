# Autor: Kaio Carmo Siqueira
# Projeto: Minha primeira página web

# importando a biblioteca
import streamlit as st

st.write('Olá Mundo!!!')
st.write('Kaio Carmo Siqueira')
st.write('--- Sistema de cálculo de IMC ---')
st.text_input('Digite seu peso: ')
st.text_input('Digite sua altura: ')
st.button('Calcular IMC')