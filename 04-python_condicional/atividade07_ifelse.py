nome = input("digite seu nome: ")
idade = input("digite sua idade : ")
prduto = float(input("digite o preço do produto:" ))

if produto >=100:
    preço = produto * 0.10
else:
    preço = produto * 0.05

    print("nome:",nome)
    print("idade: ",idade)
    print("valor calculado: ",preço)