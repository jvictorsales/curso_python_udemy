"""
Lista de listas e seus índices

Em Python, uma lista pode conter outros objetos, incluindo outras listas.
Quando uma lista contém listas em seu interior, chamamos essa estrutura de
"lista de listas".

A lista externa funciona como um contêiner principal, onde cada posição
(armazena uma referência) para uma lista interna. Cada lista interna possui
seus próprios índices, que começam em zero, assim como qualquer lista em
Python.

O acesso aos elementos é feito de forma encadeada, utilizando dois índices:
o primeiro índice seleciona a lista interna desejada e o segundo índice
seleciona o elemento dentro dessa lista.

Exemplo conceitual de acesso:
    lista[i][j]

Onde:
- i representa o índice da lista externa
- j representa o índice da lista interna

Essa estrutura é amplamente utilizada para representar dados bidimensionais,
como matrizes, tabelas, grades e mapas. Internamente, o Python não possui um
tipo nativo de matriz bidimensional; listas de listas cumprem esse papel.

É importante entender que listas são estruturas mutáveis. Isso significa que
alterações feitas em uma lista interna refletem diretamente na lista externa,
pois o que é armazenado são referências às listas internas, e não cópias
independentes.

Por fim, listas de listas podem ser percorridas com estruturas de repetição,
normalmente utilizando dois loops aninhados, permitindo acessar tanto os
valores quanto seus índices de forma controlada.
"""

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    
    # 0
    ['Elaine', ],  # 1

    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
    # ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

# print(salas)
# print(salas[1])
# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
