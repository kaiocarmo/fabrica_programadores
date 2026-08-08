# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
telefone = input('digite seu telefone: ')
cidade = input("Digite sua cidade: ")
salario = float(input("Digite seu salario: "))
if salario >= 1000:
    print("sua renda é boa ! ")
elif salario >= 700:
    print("sua renda e razoavel ! ")
elif salario >= 500:
    print("sua renda e baixa")
else:
    print("sua renda e muito baixa")