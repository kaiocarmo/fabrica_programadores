# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f"seu imc {imc:.2f} esta abaixo da tabela ")
elif imc <=24.9:
    print(f"seu imc {imc:.2f} esta agradavel")
elif imc <= 29.9:
    print(f" {imc:.2f} voce esta acima do peso indicado")
elif imc <= 34.9:
    print (f" {imc:.2f} voce se encontra em Obesidade Grau I")
elif imc <=39.9:
    print(f"{imc:.2f} voce se encontra em Obesidade Grau II")
else:
    print(f" {imc:.2f} Voce se encontra em Obesidade Grau III Procure um medico")