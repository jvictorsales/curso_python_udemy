"""
List Comprehension em Python

List comprehension é uma forma concisa e elegante de criar listas
a partir de iteráveis (como listas, tuplas, strings, ranges, etc.).
Ela permite transformar e/ou filtrar elementos em uma única linha
de código, substituindo estruturas tradicionais com for e append().

Sintaxe básica:

    [expressão for item in iterável]

Equivalente usando for tradicional:

    nova_lista = []
    for item in iterável:
        nova_lista.append(expressão)

------------------------------------------------------------

Com filtro (condição):

    [expressão for item in iterável if condição]

Isso permite incluir apenas elementos que satisfaçam
determinada regra.

------------------------------------------------------------

Com if/else na expressão:

    [valor_se_verdadeiro if condição else valor_se_falso
     for item in iterável]

Aqui, todos os elementos são processados, mas o valor
adicionado à lista depende de uma condição.

------------------------------------------------------------

Conceitos importantes:

- A expressão é executada para cada item do iterável.
- O resultado sempre será uma nova lista.
- A variável usada no for é local à comprehension.
- Pode haver mais de um for (comprehensions aninhadas),
  mas o uso excessivo pode prejudicar a legibilidade.

------------------------------------------------------------

Vantagens:

- Código mais curto e expressivo
- Geralmente mais rápido que o loop tradicional
- Mais idiomático (mais "Pythonico")

------------------------------------------------------------

Quando evitar:

- Quando a lógica ficar muito complexa
- Quando prejudicar a clareza do código
- Quando múltiplas condições deixarem a expressão confusa

------------------------------------------------------------

Resumo mental:

List comprehension = "criar lista aplicando transformação
e/ou filtro em um iterável de forma compacta".
"""


# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

lista = [num * 2 for num in range(10)]
print(list(range(10)))
print(lista)

numeros_pares = [num * 10 for num in range(10) if num % 2 == 0]
print(numeros_pares)
