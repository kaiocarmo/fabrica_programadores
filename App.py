import streamlit as st

st.title('Minha primeira página. ')
st.subheader('Feito com Streamlit ')


valor1 = st.number_input('Digite o primeiro numero: ', min_value=0.0)
valor2 = st.number_input('Digite o segundo numero: ', min_value=0.0)

if st.button('Calcular'):
    resultado = valor1 + valor2
    st.title(resultado)