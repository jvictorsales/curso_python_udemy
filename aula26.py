"""
Formatação básica de strings em Python

A formatação de strings permite inserir valores dentro de textos
de forma controlada, definindo tipo, quantidade de casas decimais,
alinhamento, preenchimento, sinal, base numérica, entre outros.

Tipos de formatação:
s  -> string (texto)
d  -> int (número inteiro decimal)
f  -> float (número de ponto flutuante)
.<n>f -> float com n casas decimais
x  -> inteiro em hexadecimal (letras minúsculas)
X  -> inteiro em hexadecimal (letras maiúsculas)

Exemplos:
{nome:s}
{idade:d}
{preco:.2f}
{numero:x}

Alinhamento e preenchimento:
(Caractere)(><^)(quantidade)

>  -> alinhamento à direita
<  -> alinhamento à esquerda
^  -> centralizado

O caractere define com o que o espaço vazio será preenchido.

Exemplos:
{valor:>10}    -> alinha à direita em 10 espaços
{valor:<10}    -> alinha à esquerda em 10 espaços
{valor:^10}    -> centraliza em 10 espaços
{valor:0>10}   -> preenche com zeros à esquerda

Sinais:
+  -> força exibição do sinal positivo ou negativo
-  -> exibe apenas o sinal negativo (padrão)

Exemplo:
{numero:+d}

Formatação numérica avançada:
,  -> separador de milhar
=  -> força o sinal a aparecer antes dos zeros

Exemplo:
{numero:0=+10,.1f}

Neste exemplo:
0   -> caractere de preenchimento
=   -> sinal vem antes dos zeros
+   -> sempre mostra o sinal
10  -> largura total
,   -> separador de milhar
.1f -> uma casa decimal

Conversion flags (conversão de valor):
!s -> str()   -> representação amigável
!r -> repr()  -> representação técnica (debug)
!a -> ascii() -> caracteres escapados

Exemplos:
{objeto!s}
{objeto!r}
{objeto!a}

Essas regras funcionam tanto com str.format()
quanto com f-strings (recomendado).
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.487867868976:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
