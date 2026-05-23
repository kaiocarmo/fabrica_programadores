nome = input('digite seu nome')
idade = input('digite sua idade: ')
cnh = input('voce possui cnh sim ou não ')
if idade >= 18 :
    if cnh == 'sim':
        print(f'{nome} voce pode dirigir ')
    else:
print(f'{nome} voce não pode dirigir')
else:
    print(f'{nome} voce é menor de idade ')