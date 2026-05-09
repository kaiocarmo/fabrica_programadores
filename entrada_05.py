# Autor: Kaio Carmo Siqueira
# Projeto: Entrada com input e f-string

# Declaração de variáveis
nome = input("Digite seu nome: ")
valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
soma = valor1 + valor2
subtração = valor1 - valor2
divisão = valor1 / valor2
multiplicação = valor1 * valor2

# exibindo os resultados com f-string
print(nome)
print(f"o resultado da soma é: {soma}")
print(f"o resultado da subtracao é: {subtração}")
print(f"o resultado da divisao é : {divisão}")
print(f"o resultado da multiplicacao é: {multiplicação}")