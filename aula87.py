"""
isinstance() — Verificando o tipo de um objeto em Python

A função isinstance() é utilizada para verificar se um objeto
é instância de um determinado tipo (classe).

Sintaxe:
    isinstance(objeto, tipo)

Retorno:
    True  -> se o objeto for do tipo informado
    False -> caso contrário

Também é possível verificar múltiplos tipos passando uma tupla:

    isinstance(objeto, (tipo1, tipo2, tipo3))

Exemplos básicos:

    x = 10
    isinstance(x, int)      # True
    isinstance(x, str)      # False

Múltiplos tipos:

    x = 10
    isinstance(x, (int, float))  # True

Diferença entre isinstance() e type():

    type(x) == int
        - Verifica o tipo EXATO do objeto.

    isinstance(x, int)
        - Verifica se o objeto é daquele tipo OU de uma classe
          que herda daquele tipo (suporta herança).

Exemplo com herança:

    class Animal:
        pass

    class Cachorro(Animal):
        pass

    rex = Cachorro()

    isinstance(rex, Animal)  # True
    type(rex) == Animal      # False

Observação importante:
    bool é subtipo de int em Python:

        isinstance(True, int)  # True

Quando usar:
    - Para validar entradas de funções
    - Para criar comportamentos diferentes dependendo do tipo
    - Para trabalhar com herança em Programação Orientada a Objetos

Boas práticas:
    Prefira isinstance() em vez de comparar com type(),
    pois ele é mais flexível e respeita herança.
"""

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'João'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print('STR')
        print(item.upper())
    
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)
