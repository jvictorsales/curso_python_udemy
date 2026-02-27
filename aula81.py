"""
Função lambda em Python

A função lambda é uma forma de criar funções anônimas (sem nome)
de maneira curta e direta. Ela é utilizada quando precisamos de
uma função simples, geralmente usada por pouco tempo ou passada
como argumento para outra função.

Diferente das funções definidas com "def", a lambda:

- Não possui nome próprio (a menos que seja atribuída a uma variável).
- Contém apenas uma única expressão.
- Não utiliza a palavra-chave "return".
- Retorna automaticamente o resultado da expressão definida.

Sua estrutura é:

    lambda parametros: expressao

A expressão deve ser única, ou seja, não é possível colocar
múltiplas instruções, laços, ou comandos como if/else tradicionais
(em bloco). Apenas expressões são permitidas.

Funções lambda são muito utilizadas junto com funções de ordem
superior, como sorted(), map() e filter(), onde pequenas funções
são necessárias apenas para definir um comportamento específico.

Embora sejam práticas e elegantes para casos simples, lambdas
devem ser usadas com cuidado. Quando a lógica começa a ficar
complexa, o ideal é utilizar uma função tradicional com "def"
para manter a legibilidade e organização do código.

Em resumo, lambda é uma ferramenta para criar funções curtas,
objetivas e descartáveis, aproveitando o fato de que funções em
Python são objetos de primeira classe.
"""

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort()
# print(lista)
# lista.sort(reverse=True)
# print(lista)
# lista_2 = sorted(lista)
# print(lista_2)

lista = [
    {'nome': 'João', 'sobrenome': 'Sales'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

def exibir(lista):
    for item in lista:
        print(item)
    print()

# lista.sort(key=ordena)

# lista.sort(key=lambda item: item['nome'])

lista_ordenada_1 = sorted(lista, key=lambda item: item['nome'])
lista_ordenada_2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista_ordenada_1)
exibir(lista_ordenada_2)
