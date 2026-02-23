"""
*args — Argumentos não nomeados em Python

Em Python, *args é utilizado na definição de funções para permitir
a passagem de uma quantidade variável de argumentos posicionais
(não nomeados).

O operador * realiza o empacotamento (packing) desses argumentos,
reunindo todos os valores adicionais passados para a função
em uma tupla.

Dessa forma, a função pode receber zero ou mais argumentos
posicionais sem que seja necessário definir previamente
quantos parâmetros ela irá aceitar.

O mesmo operador * também pode ser usado para o desempacotamento
(unpacking), que consiste em extrair os valores de uma sequência
(como listas ou tuplas) e passá-los individualmente como argumentos
para uma função.

Em resumo:
- *args empacota múltiplos argumentos posicionais em uma tupla.
- O operador * pode desempacotar uma sequência ao passá-la
  como argumentos para uma função.
"""

# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)
print(*resto)

def somar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

lista = [1,2,3,4,5]
resultado = somar(*lista)
resultado = somar(1,2,3,4,5)
print(resultado)

print(sum(lista))
print(sum((1,2,3,4,5)))
