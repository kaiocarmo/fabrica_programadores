# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
def calcular (peso,altura):
    imc = peso / (altura * altura) 
    if imc <= 18.5:
        print('seu IMC esta agradavel')
    else:
        print('você se encontra acima do peso')
calcular(peso,altura)