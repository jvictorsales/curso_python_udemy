"""
Iterables, Iterators e Generators em Python
===========================================

Python utiliza um mecanismo chamado **protocolo de iteração**
para percorrer objetos como listas, strings e dicionários.

Esse protocolo envolve três conceitos principais:

    1. Iterable
    2. Iterator
    3. Generator


----------------------------------------------------------------
1) ITERABLE
----------------------------------------------------------------

Um **iterable** é qualquer objeto que pode ser percorrido
elemento por elemento.

Exemplos comuns de iterables:

    list
    tuple
    set
    dict
    str
    range

Esses objetos podem ser usados em um loop `for` porque
implementam o método especial:

    __iter__()

Esse método retorna um **iterator**.

Exemplo:

    lista = [1, 2, 3]

    for item in lista:
        print(item)

Um iterable **não precisa implementar `__next__()`**.
Ele apenas precisa saber **criar um iterator**.

Podemos verificar isso:

    lista = [1, 2, 3]

    hasattr(lista, "__iter__")   # True
    hasattr(lista, "__next__")   # False

Portanto:

    list = iterable
    list ≠ iterator


----------------------------------------------------------------
2) ITERATOR
----------------------------------------------------------------

Um **iterator** é o objeto responsável por retornar os
elementos um por vez durante a iteração.

Ele implementa dois métodos principais:

    __iter__()
    __next__()

O método `__next__()` retorna o próximo valor da sequência.

Exemplo:

    lista = [10, 20, 30]

    it = iter(lista)

    print(next(it))  # 10
    print(next(it))  # 20
    print(next(it))  # 30

Quando os valores acabam, Python levanta a exceção:

    StopIteration

Importante:

    Todo iterator também é um iterable.

Isso acontece porque o método `__iter__()` de um iterator
simplesmente retorna ele mesmo.

Exemplo:

    it = iter([1, 2, 3])

    iter(it) is it   # True


----------------------------------------------------------------
3) PROTOCOLO DE ITERAÇÃO
----------------------------------------------------------------

O loop `for` utiliza internamente o seguinte processo:

    iterable --iter()--> iterator --next()--> valores

Equivalente a:

    iterator = iter(iterable)

    while True:
        try:
            valor = next(iterator)
            print(valor)
        except StopIteration:
            break


----------------------------------------------------------------
4) GENERATOR EXPRESSIONS
----------------------------------------------------------------

Generator expressions são uma forma compacta de criar
**generators**, que são um tipo especial de iterator.

Sintaxe:

    (expressao for item in iteravel)

Exemplo:

    gen = (x * 2 for x in range(5))

Diferente das list comprehensions, os generators NÃO
armazenam todos os valores na memória.

Eles produzem valores **sob demanda**.

Uso:

    gen = (x * 2 for x in range(5))

    print(next(gen))  # 0
    print(next(gen))  # 2
    print(next(gen))  # 4


----------------------------------------------------------------
5) GENERATOR FUNCTIONS (yield)
----------------------------------------------------------------

Generators também podem ser criados usando funções com
a palavra-chave `yield`.

Exemplo:

    def contador(n):
        i = 0
        while i < n:
            yield i
            i += 1

Uso:

    gen = contador(3)

    print(next(gen))  # 0
    print(next(gen))  # 1
    print(next(gen))  # 2

Uma função que utiliza `yield` não retorna uma lista.
Ela retorna um **generator object**, que é um iterator.


----------------------------------------------------------------
6) LIST COMPREHENSION vs GENERATOR EXPRESSION
----------------------------------------------------------------

List comprehension:

    lista = [x * 2 for x in range(5)]

Resultado:

    [0, 2, 4, 6, 8]

Todos os valores são criados imediatamente na memória.

Generator expression:

    gen = (x * 2 for x in range(5))

Resultado:

    <generator object ...>

Os valores são gerados apenas quando necessários.


----------------------------------------------------------------
7) CONSUMO DE GENERATORS
----------------------------------------------------------------

Generators são consumidos conforme são iterados.

Exemplo:

    gen = (x for x in range(3))

    print(list(gen))
    print(list(gen))

Saída:

    [0, 1, 2]
    []

Isso acontece porque o iterator já foi completamente percorrido.


----------------------------------------------------------------
8) RESUMO
----------------------------------------------------------------

Iterable
    objeto que pode criar um iterator
    possui __iter__()

Iterator
    objeto que produz valores um por vez
    possui __iter__() e __next__()

Generator
    tipo especial de iterator criado por:
        - generator expressions
        - funções com yield

Fluxo do protocolo de iteração:

    iterable --iter()--> iterator --next()--> valores
"""

import sys

iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__()  # tem __iter__ e __next__
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print()

lista = [num for num in range(1000000)]
print('Lista:', sys.getsizeof(lista))

generator = (num for num in range(1000000))
# print(generator)  # Generator Object
print('Generator:', sys.getsizeof(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for n in generator:
#     print(n)
