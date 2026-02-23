"""
Interpolação básica de strings em Python

Interpolação de strings é o processo de inserir valores dentro de uma string
de forma dinâmica, substituindo marcadores por dados reais no momento da
formatação.

No Python, uma das formas clássicas de interpolação utiliza o operador `%`,
no qual símbolos especiais indicam o tipo de dado que será inserido na string.

Especificadores de formatação:

s  - string
     Converte o valor para texto usando sua representação padrão.

d  - inteiro (decimal)
i  - inteiro
     Utilizados para representar números inteiros.

f  - ponto flutuante (float)
     Representa números reais, podendo ser configurado para exibir
     uma quantidade específica de casas decimais.

x  - hexadecimal (letras minúsculas)
X  - hexadecimal (letras maiúsculas)
     Converte números inteiros para a base hexadecimal
     (ABCDEF0123456789).

Funcionamento geral:
A string contém os especificadores de formatação e, após o operador `%`,
são passados os valores que substituirão esses marcadores, respeitando
a ordem e o tipo esperado.

Observação:
Apesar de ainda funcionar, esse estilo de interpolação é considerado
legado. Atualmente, o uso de `str.format()` e, principalmente, f-strings
é recomendado por oferecer melhor legibilidade e manutenção do código.
"""

nome = 'João'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (1500, 1500))
