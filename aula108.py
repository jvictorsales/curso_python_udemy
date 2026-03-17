"""
itertools.count

count é um iterador infinito da biblioteca padrão do Python (módulo itertools)
que gera números de forma contínua. Ele começa em um valor inicial (start)
e vai incrementando esse valor de acordo com o passo definido (step).

Por ser um iterador infinito, ele nunca para de gerar valores sozinho.
Por isso, normalmente é utilizado junto com estruturas de controle
(como break) ou funções que limitam a iteração.

Parâmetros:
    start (int | float, opcional):
        Valor inicial da sequência. O padrão é 0.

    step (int | float, opcional):
        Valor que será somado a cada iteração. O padrão é 1.

Retorno:
    Um iterador infinito que produz números sucessivos.

Observação:
    Como count é infinito, tenha cuidado ao utilizá-lo em loops
    para evitar execuções intermináveis.
"""

from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)
# print(next(c1))
# print(next(c1))
# print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()

print('range')
for i in r1:
    print(i)

print()

nomes = ['Ana', 'João', 'Maria']
for i, nome in zip(count(1), nomes):
    print(i, nome)
