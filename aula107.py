"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [10, 2, 3, 40, 50, 60, 70]
lista_b = [1, 2, 3, 4]

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# menor_tamanho_entre_as_listas = len(lista_a) if len(lista_a) < len(lista_b) else len(lista_b)
# lista_soma = []
# for i in range(menor_tamanho_entre_as_listas):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# for i in range(min(len(lista_a), len(lista_b))):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# lista_de_tuplas = list(zip(lista_a, lista_b))
# for tupla in lista_de_tuplas:
#     soma = 0
#     for item in tupla:
#         soma += item
#     lista_soma.append(soma)
# print(lista_soma)

# menor_lista = lista_a if len(lista_a) < len(lista_b) else lista_b
# lista_soma = []
# for i, _ in enumerate(menor_lista):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# for x, y in zip(lista_a, lista_b):
#     lista_soma.append(x + y)
# print(lista_soma)

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

from itertools import zip_longest
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)
