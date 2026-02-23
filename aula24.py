"""
Operadores `in` e `not in` em Python

Os operadores `in` e `not in` são usados para verificar **pertencimento**
(membership) em objetos iteráveis.

Um objeto iterável é qualquer estrutura que pode ser percorrida elemento
por elemento, como strings, listas, tuplas, conjuntos e dicionários.

- `in` retorna True se o valor estiver presente no iterável.
- `not in` retorna True se o valor NÃO estiver presente no iterável.

No caso das strings, elas são iteráveis por caracteres.
Cada caractere possui um índice associado, começando em 0 (da esquerda
para a direita) e também índices negativos (da direita para a esquerda).

Exemplo de índices em uma string:

    Índices positivos:
      0 1 2 3 4 5
      V i c t o r

    Índices negativos:
     -6 -5 -4 -3 -2 -1
      V  i  c  t  o  r

Os operadores `in` e `not in` não trabalham diretamente com índices,
mas sim verificando se um caractere (ou valor) existe em qualquer posição
do iterável.

Esses operadores são muito úteis para:
- Verificar se um caractere existe em uma string
- Verificar se um valor existe em uma lista ou tupla
- Verificar chaves em dicionários
- Tornar condições mais legíveis e expressivas

O uso correto de `in` e `not in` ajuda a deixar o código mais claro,
evitando comparações repetitivas e desnecessárias.
"""

nome = 'Victor'
# print(nome[5])
# print(nome[-1])
print('Vic' in nome)
print('blue' in nome)
print(10 * '-')
print('Vic' not in nome)
print('blue' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
