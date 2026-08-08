# Autor: Kaio Carmo Siqueira
# Projeto: Condicionais

# Definição das variáveis
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float (input("Digite a segunda nota "))
if nota1 >= 6:
    print("Voce passou ! ")
elif nota2 <= 6:
    print("Voce em recuperacao ! ")
else:
    print("Aluno reprovado! ")