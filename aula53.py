"""
enumerate - enumera iteráveis (índices)
"""


lista = ['Maria', 'Helena', 'João']
lista.append('Luiz')

lista_enumerada = enumerate(lista)

# print(lista_enumerada)
# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(next(lista_enumerada))  # StopIteration

# for item in lista_enumerada:
#     print(item)

# print('Segundo for não tem mais nada para iterar.')
# for item in lista_enumerada:
#     print(item)


# for item in enumerate(lista):
#     print(item)

# print()

# for item in enumerate(lista):
#     print(item)


# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for item in lista_enumerada:
#     print(item)

# for item in lista_enumerada:
#     print(item)


# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
