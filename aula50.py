"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 João
"""

lista = ['Maria', 'Helena', 'João']

lista.append('Luiz')

i = 0
for nome in lista:
    print(i, nome, type(nome))
    i += 1

print()

for indice, nome in enumerate(lista):
    print(indice, nome, type(nome))

print()

indices_lista = range(len(lista))
for indice in indices_lista:
    print(indice, lista[indice], type(lista[indice]))
