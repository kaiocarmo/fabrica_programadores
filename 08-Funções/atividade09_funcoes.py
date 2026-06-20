numero = int(input('digite um numero da tabuada: '))
def calcular(numero):
    i = 1
    while i <= 10:
        print(f' {numero} x {i} = {numero * i} ')
        i = i +1
calcular(numero)