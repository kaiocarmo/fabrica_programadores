# Autor: Kaio Carmo Siqueira
# Projeto: Minha primeira página web

# importando a biblioteca
import streamlit as st

st.title('--- Sistema de cálculo de IMC ---')
peso = st.number_input('Digite seu peso: ')
altura = st.number_input('Digite sua altura: ')
if st.button('Calcular IMC'):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        st.success(f'Seu IMC é: {imc:.2f}', icon="✅")
        if imc < 18.5:
            st.error('Abaixo do peso', icon="🚨")
        elif imc < 24.9:
            st.success('Peso normal', icon="✅")
        elif imc <= 29.9:
            st.warning('Sobrepeso', icon="⚠️")
        elif imc <= 34.9:
            st.warning('Obesidade Grau I', icon="⚠️")
        elif imc <= 39.9:
            st.warning('Obesidade Grau II', icon="⚠️")
        else:
            st.error('Obesidade Grau III (morbída)', icon="🚨")
    else:
        st.error('Digite um número válido!', icon="🚨")