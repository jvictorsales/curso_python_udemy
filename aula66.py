"""
Argumentos nomeados e não nomeados em funções Python

Em Python, ao chamar uma função, podemos passar argumentos
de duas formas principais: posicionais (não nomeados) e
nomeados (keyword arguments).

Argumentos posicionais são atribuídos aos parâmetros da
função de acordo com a ordem em que foram definidos.
Por isso, a posição é importante e deve ser respeitada.

Argumentos nomeados são passados informando explicitamente
o nome do parâmetro seguido do sinal de igual (=). Nesse
caso, a ordem não é obrigatória, pois cada valor é associado
diretamente ao seu respectivo parâmetro pelo nome.

Também é possível misturar os dois tipos na mesma chamada,
desde que os argumentos posicionais venham antes dos
argumentos nomeados.

Além disso, funções podem ter parâmetros com valores padrão.
Quando um argumento não é informado, o valor padrão definido
na função é utilizado.
"""

def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3)
soma(2, 1, 3)
soma(y=2, z=3, x=1)
soma(1, 2, z=5)
soma(1, y=2, z=5)
