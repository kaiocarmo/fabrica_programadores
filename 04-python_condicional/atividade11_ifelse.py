# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
cidade = input ("Digite sua Cidade : ")
cnh = input ("voce tem cnh (sim ou não): ")
if cnh == 'sim':
    print("voce pode dirigir ! ")
elif idade <= 18:
    print ("voce e menor de idade! ")
else:
    print("voce nao pode dirigir! ")