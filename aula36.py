"""
Operadores de atribuição em Python

Os operadores de atribuição são utilizados para atribuir valores a variáveis.
Além da atribuição simples, existem operadores que combinam uma operação
aritmética com a atribuição, tornando o código mais curto e legível.

Operador "="
Atribui um valor diretamente a uma variável.
Exemplo:
x = 10

Operadores de atribuição compostos:
Esses operadores realizam uma operação usando o valor atual da variável
e, em seguida, armazenam o resultado na própria variável.

+=  Soma e atribui
    x += 2  -> equivalente a: x = x + 2

-=  Subtrai e atribui
    x -= 2  -> equivalente a: x = x - 2

*=  Multiplica e atribui
    x *= 2  -> equivalente a: x = x * 2

/=  Divide e atribui (divisão com resultado float)
    x /= 2  -> equivalente a: x = x / 2

//= Divide e atribui (divisão inteira)
     x //= 2 -> equivalente a: x = x // 2

**= Eleva à potência e atribui
     x **= 2 -> equivalente a: x = x ** 2

%=  Calcula o resto da divisão e atribui
     x %= 2  -> equivalente a: x = x % 2

Esses operadores ajudam a deixar o código mais enxuto,
reduzem repetições e melhoram a legibilidade, principalmente
em operações acumulativas.
"""

contador = 10

while contador >= 0:
    print(contador)
    contador -= 1

print('Acabou')


repetidor = 10
repetidor *= '2'
print(repetidor)
