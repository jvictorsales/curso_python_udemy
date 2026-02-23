"""
Operadores de comparação (ou relacionais) são usados para comparar dois valores.
O resultado de qualquer operação de comparação em Python é sempre um valor
booleano: True (verdadeiro) ou False (falso).

Esses operadores são amplamente utilizados em estruturas de decisão
(if, elif, else), laços de repetição (while, for) e em expressões lógicas,
permitindo que o programa tome decisões com base em condições.

Principais operadores de comparação em Python:

>   Maior que
    Verifica se o valor à esquerda é maior que o valor à direita.

>=  Maior ou igual a
    Verifica se o valor à esquerda é maior ou igual ao valor à direita.

<   Menor que
    Verifica se o valor à esquerda é menor que o valor à direita.

<=  Menor ou igual a
    Verifica se o valor à esquerda é menor ou igual ao valor à direita.

==  Igual a
    Verifica se os dois valores são iguais.
    Atenção: este operador compara valores, não atribui.
    (Não confundir com o operador de atribuição =)

!=  Diferente de
    Verifica se os dois valores são diferentes.

Os operadores de comparação podem ser usados com diversos tipos de dados,
como números, strings e valores booleanos, respeitando as regras internas
de comparação de cada tipo.

Em resumo, operadores relacionais permitem avaliar condições e são
fundamentais para o controle do fluxo de execução de um programa.
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(diferente)
