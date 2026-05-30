# Autor: Kaio Carmo Siqueira
# Projeto: Loop FOR

numero = int(input('escolha um numero da tabuada: '))
inicio = int(input('escolha o primeiro numero: '))
fim = int(input('escolha o ultimo numero: '))

for i in range(inicio,fim+1):
    print(f' {numero} x {i} = {numero * i} ')
if numero == 2 * i:
    print('resultado') 
else:
    print("erro")