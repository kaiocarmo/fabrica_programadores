# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f"seu imc {imc} esta abaixo da tabela ")
elif imc <=24.9:
    print(f"seu imc {imc} esta agradavel")
elif imc <= 29.9:
    print(f" {imc} voce esta acima do peso indicado")
elif imc <= 34.9:
    print (f" {imc} voce se encontra em Obesidade Grau I")
elif imc <=39.9:
    print(f"{imc} voce se encontra em Obesidade Grau II")
else:
    print(f" {imc} Voce se em Obesidade Grau III Procure um medico")