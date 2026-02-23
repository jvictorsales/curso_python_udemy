"""
Imprecisão de ponto flutuante em Python

Em Python (e na maioria das linguagens), números do tipo float não são
armazenados de forma exata. Isso acontece porque o Python utiliza o
padrão IEEE 754 de dupla precisão (double-precision floating-point format)
para representar números de ponto flutuante na memória.

Esse padrão armazena os números em base binária (potências de 2),
enquanto muitos números que usamos no dia a dia são representados em
base decimal (potências de 10). Como consequência, vários valores
decimais simples, como 0.1, 0.2 ou 0.3, não possuem uma representação
binária finita e acabam sendo aproximados.

Por causa dessas aproximações, operações aparentemente simples podem
gerar resultados inesperados. Por exemplo:
    0.1 + 0.2 != 0.3

Isso não é um erro do Python, mas uma limitação matemática da forma como
os floats são representados no computador.

Características importantes da imprecisão de ponto flutuante:
- Floats são aproximações, não valores exatos.
- Pequenos erros podem se acumular em cálculos sucessivos.
- Comparações diretas entre floats usando '==' podem falhar.
- O resultado exibido é arredondado para facilitar a leitura, mas o
  valor real armazenado pode conter mais casas decimais.

Boas práticas para lidar com floats:
- Evitar comparações diretas de igualdade entre floats.
- Usar uma tolerância (epsilon) ao comparar valores.
- Para cálculos financeiros ou que exigem precisão exata, usar o módulo
  decimal (Decimal) ou trabalhar com inteiros (ex: centavos em vez de reais).

Referências:
- https://en.wikipedia.org/wiki/Double-precision_floating-point_format
- https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""


import math
# import decimal
from decimal import Decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(f'Usando o método round() = {round(numero_3, 2)}')

print(10 * '-')

print('Multiplicando os valores por 10 e depois dividindo')
numero_1 = 0.1 * 10
numero_2 = 0.7 * 10
numero_3 = (numero_1 + numero_2) / 10
print(numero_3)

print(10 * '-')

print('Usando math.isclose() - (comparações seguras)')
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(math.isclose(numero_3, 0.8))

print(10 * '-')

print('Usando Decimal - (financeiro, precisão alta)')
numero_1 = Decimal('0.1')
numero_2 = Decimal('0.7')
numero_3 = numero_1 + numero_2
print(f'A soma de {numero_1} + {numero_2} = {numero_3}')
