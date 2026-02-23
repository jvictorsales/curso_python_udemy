"""
Valores padrão para parâmetros

Em Python, parâmetros de funções podem possuir valores padrão.
Esses valores são utilizados automaticamente quando o argumento
correspondente não é informado na chamada da função.

Parâmetros com valores padrão tornam-se opcionais, enquanto
parâmetros sem valores padrão permanecem obrigatórios.

Uma regra fundamental é que parâmetros com valores padrão devem
sempre ser definidos após os parâmetros obrigatórios, para que
o interpretador consiga associar corretamente os argumentos.

Os valores padrão são avaliados apenas uma vez, no momento em que
a função é definida, e não a cada chamada. Por esse motivo, o uso
de objetos mutáveis como valores padrão pode causar efeitos
colaterais inesperados entre diferentes execuções da função.

Como boa prática, recomenda-se utilizar valores imutáveis ou
None como valor padrão e inicializar objetos mutáveis dentro
do corpo da função quando necessário.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=}', '|', 'x + y =', x + y)

soma(2, 5)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
