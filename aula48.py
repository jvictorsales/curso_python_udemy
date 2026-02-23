"""
Listas em Python

Listas são estruturas de dados do tipo `list` e são **mutáveis**, ou seja,
seus valores podem ser alterados após a criação. Elas permitem armazenar
múltiplos valores em uma única variável, inclusive valores de **tipos
diferentes** (int, float, str, bool, outras listas, etc).

As listas reutilizam conhecimentos já vistos em strings, como:
- Índices (positivos e negativos)
- Fatiamento (slice)

Isso permite acessar, modificar ou extrair partes da lista de forma simples
e eficiente.

Principais métodos e operações com listas:

- append(valor)
  Adiciona um item ao final da lista.

- insert(indice, valor)
  Insere um item em uma posição específica da lista.

- pop()
  Remove e retorna o último item da lista.
  Também pode remover um item de um índice específico.

- del
  Remove um item da lista a partir do índice informado.

- clear()
  Remove todos os itens da lista, deixando-a vazia.

- extend(iterável)
  Adiciona vários elementos de outro iterável à lista.

- Operador +
  Concatena duas listas, criando uma nova lista.

Listas seguem o conceito de CRUD:
- Create (Criar): adicionar elementos
- Read (Ler): acessar elementos
- Update (Atualizar): modificar elementos
- Delete (Apagar): remover elementos

Essas operações são realizadas principalmente por meio de índices:
lista[i]

Por serem mutáveis e muito flexíveis, listas são uma das estruturas
de dados mais usadas em Python.
"""


# #        +01234
# #        -54321
# string = 'ABCDE'  # 5 caracteres (len)

# # lista = []  # ''
# # print(lista, type(lista))
# # print(bool(lista))  # falsy

# #        0    1      2             3    4
# #       -5   -4     -3            -2   -1
# lista = [123, True, 'João Victor', 1.2, []]
# # print(lista)
# # print(lista[2].upper(), type(lista[2]))
# # print(lista[-2], type(lista[-2]))


# print(lista[2])
# print(lista)

# lista[2] = 'Ruth Batista'

# print(lista[2])
# print(lista)



# #        0   1   2   3
# lista = [10, 20, 30, 40]
# print(lista)
# lista[2] = 50
# print(lista)

# numero = lista[2]
# print(numero)

# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50)
# lista.append(60)
# lista.append(70)
# print(lista)
# ultimo_valor = lista.pop()
# print(lista)
# print('Removido:', ultimo_valor)

# lista.pop(3)
# print(lista)


#        0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append('João')
# print(lista)
# ultimo_item = lista.pop()
# print(lista, ultimo_item)
# lista.append(1233)
# print(lista)
# del lista[-1]
# print(lista)
# lista.clear()
# print(lista)

# lista.insert(0, 'João')
# print(lista)

# lista.insert(100, 5)
# print(lista)
# print(lista[5])
# # print(lista[100])  # IndexError


# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# print(lista_a)
# print(lista_b)
# print(lista_c)

# lista_a.extend(lista_b)
# print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'João'
nome_2 = nome
print(nome, nome_2)
print(id(nome), id(nome_2))

nome += 'Silva'
print(nome, nome_2)
print(id(nome), id(nome_2))

print()

lista_1 = [1, 2, 3]
lista_2 = lista_1
print(lista_1, id(lista_1))
print(lista_2, id(lista_2))

lista_1.append(4)

print()
print(lista_1, id(lista_1))
print(lista_2, id(lista_2))

print()
lista_3 = list(lista_1)
print(lista_3, id(lista_3))

lista_4 = lista_1[::]
print(lista_4, id(lista_4))

lista_5 = lista_1.copy()
print(lista_5, id(lista_5))
