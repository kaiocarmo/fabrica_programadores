# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura)
if imc <= 18.5:
    print("seu imc esta agradavel ")
else:
    print("Voce se encontra acima do peso! ")