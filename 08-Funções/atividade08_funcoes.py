# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))
def calcular(nota):
    if nota >= 6:
        print("Aluno Aprovado! ")
    else:
        print("Aluno Reprovado! ")
calcular(nota)