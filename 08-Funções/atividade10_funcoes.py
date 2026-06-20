numero = int(input('digite um numero da tabuada: '))
i = int(input('digite o primeiro numero: '))
fim = int(input('digite o ultimo numero: '))
def calcular(numnero):
    i = 1

    while i <= fim:
        print(f' {numero} x {i} = {numero * i} ')
        i = i +1
calcular(numero)