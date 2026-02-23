"""
Fatiamento de strings em Python

Strings em Python são sequências ordenadas e imutáveis de caracteres.
Isso significa que cada caractere possui um índice e pode ser acessado
individualmente ou em partes, por meio do fatiamento (slice).

Índices:
Os índices começam em 0 para o primeiro caractere e vão até len(string) - 1.
Também é possível utilizar índices negativos, que começam em -1 e contam
a partir do final da string.

Exemplo de índices:
  0 1 2 3 4 5 6 7 8
  O l á   M u n d o
 -9-8-7-6-5-4-3-2-1

Sintaxe do fatiamento:
string[início:fim:passo]

- início (i): índice onde o fatiamento começa (inclusivo).
- fim (f): índice onde o fatiamento termina (exclusivo).
- passo (p): intervalo entre os caracteres selecionados.

Observações importantes:
- O índice final (fim) não é incluído no resultado.
- Se o início for omitido, o fatiamento começa do índice 0.
- Se o fim for omitido, o fatiamento vai até o final da string.
- Se o passo for omitido, o valor padrão é 1.
- Usar um passo negativo permite inverter a string.

Forma abreviada:
[i:f:p] ou [::]

Função len():
A função len(string) retorna a quantidade de caracteres da string e é
muito útil para determinar limites de fatiamento e evitar erros de índice.

Como strings são imutáveis, o fatiamento não altera a string original,
apenas retorna uma nova string com o trecho selecionado.
"""


variavel = 'Olá Mundo'
# print(variavel[-4])
print(variavel[4:])
print(variavel[4:8])
print(variavel[:5])
print(variavel[0:5])
print(variavel[-9:-4])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[::-2])
