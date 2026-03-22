# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes da barra deve
# ser APENAS posicional.
# PEP 570 - Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores.
# PEP 3102 - Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# def soma(a, b, /, x, y):
# def soma(a, b, *, x, y):
# def soma(a, b, /, *, x, y):
# def soma(a, b, /, *, x, y, **kwargs):
def soma(a, b, /, c, *, x, y, **kwargs):
    print(kwargs)
    print(f'{c=}')
    return a + b + x + y

# print(soma(1, 2, 3, y=4))
# print(soma(1, 2, x=3, y=4))
# print(soma(1, 2, x=3, y=4, z=5))
print(soma(1, 2, 2.5, x=3, y=4, z=5))
print()
print(soma(1, 2, c=2.5, x=3, y=4, z=5))
