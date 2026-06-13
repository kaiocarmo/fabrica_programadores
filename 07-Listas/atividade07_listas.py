# Autor: Kaio Carmo Siqueira
# Projeto: Listas

penta = ['Brasil','paraguay', 'chlie']
tetra = ['Brasil', 'Italia', 'Alemanha']
tri = ['Brasil', 'Italia', 'Alemanha', 'Ermanos']

# Imprimindo os nomes
print('---Campeões do Mundo---')

# excluindo por posição
# exemplo: excluir o chile
del penta[2]
print(penta)
# excluindo por nome
print(penta)
penta.remove('paraguay')
print(penta)