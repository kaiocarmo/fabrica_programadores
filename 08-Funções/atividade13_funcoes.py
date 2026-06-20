# Autor: Kaio Carmo Siqueira
# Projeto: Listas

penta = ['Brasil','paraguay', 'chile']
tetra = ['Brasil', 'Italia', 'Alemanha']
tri = ['Brasil', 'Italia', 'Alemanha', 'Ermanos']
pais = input('Digite o pais que deseja adicionar: ')

def adicionar(batata):

# Imprimindo os nomes
    print('---Campeões do Mundo---')
# excluindo por nome
    print(penta)
    penta.append(pais)
    print(penta)
adicionar(pais)