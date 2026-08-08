nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
cnh = input('voce possui CNH sim ou não: ')
if idade >= 18 :
    if cnh == 'sim':
        print(f'{nome} voce pode dirigir ')
    else:
        print(f'{nome} voce NÃO pode dirigir')
else:
    print(f'{nome} voce é menor de idade ')