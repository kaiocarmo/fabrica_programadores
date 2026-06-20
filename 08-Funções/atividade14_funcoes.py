# Autor: Kaio Carmo Siqueira
# Projeto: Listas

penta = ['Brasil','paraguay', 'chile']
tetra = ['Brasil', 'Italia', 'Alemanha']
tri = ['Brasil', 'Italia', 'Alemanha', 'Ermanos']
pais = input('Digite o pais que deseja remover: ')

def remover(pais):

# Imprimindo os nomes
    print('---Campeões do Mundo---')
# excluindo por nome
    print(penta)
    penta.remove(pais)
    print(penta)
remover(pais)