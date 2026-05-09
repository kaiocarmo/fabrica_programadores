# Autor: Kaio Carmo Siqueira
# Projeto: IMC com input e f-string

# Declaração de variáveis
peso = float(input("digite o peso: "))
altura = float(input("digite sua altura: "))
IMC = peso / (altura * altura)

# exibindo os resultados
print(f"o resultado do IMC é: {IMC}")