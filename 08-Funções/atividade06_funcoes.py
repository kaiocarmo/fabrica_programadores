# Autor: Kaio Carmo Siqueira
# Projeto: Entrada com input

# Declaração de variáveis
valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: ")) 

#função calcular - 4 operações básicas
def calcular(valor1,valor2):
    somar = valor1+valor2
    subtrair = valor1-valor2
    multiplicar = valor1*valor2
    dividir = valor1/valor2
    print(f'O resultado da soma é: {somar}')
    print(f'O resultado da subtração é: {subtrair}')
    print(f'O resultado da multiplicão é: {multiplicar}')
    print(f'O resultado da divisão é: {dividir}')

# Chamada da Função
calcular(valor1,valor2)