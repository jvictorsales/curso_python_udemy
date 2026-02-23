"""
Ordem de precedência dos operadores em Python

A ordem de precedência define a sequência em que os operadores são avaliados
em uma expressão quando não há parênteses suficientes para eliminar
ambiguidades. Operadores com maior precedência são avaliados primeiro,
antes dos operadores de menor precedência.

Em Python, a precedência básica segue esta hierarquia (da maior para a menor):

1. Parênteses: ( )
   Expressões entre parênteses sempre são avaliadas primeiro.
   Eles permitem controlar explicitamente a ordem de execução.

2. Exponenciação: **
   Calcula potências. Possui precedência maior que multiplicação e adição.

3. Operadores multiplicativos: *, /, //, %
   Incluem multiplicação, divisão, divisão inteira e módulo.
   São avaliados após a exponenciação e antes da adição/subtração.

4. Operadores aditivos: +, -
   Incluem soma e subtração.
   São avaliados por último entre os operadores aritméticos básicos.

Quando operadores possuem a mesma precedência, a avaliação ocorre,
em geral, da esquerda para a direita, com exceção da exponenciação (**),
que é associativa da direita para a esquerda.

O uso de parênteses é considerado uma boa prática para tornar o código
mais legível e evitar interpretações equivocadas da ordem de cálculo.
"""

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
