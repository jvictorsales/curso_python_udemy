"""
Retorno de valores das funções (return)

Em Python, o comando `return` é utilizado para encerrar a execução de uma função
e devolver um valor ao ponto onde a função foi chamada. Esse valor pode ser de
qualquer tipo de dado suportado pela linguagem, como números, strings, listas,
tuplas, dicionários, objetos ou até mesmo outras funções.

Quando uma função executa um `return`, todo o código abaixo dele não é executado,
pois a função é finalizada imediatamente. Caso uma função não possua a instrução
`return`, ou utilize apenas `return` sem especificar um valor, ela retornará
implicitamente o valor `None`.

Uma função pode retornar mais de um valor utilizando estruturas como tuplas,
o que permite que múltiplos dados sejam devolvidos em uma única chamada. O valor
retornado por uma função pode ser armazenado em uma variável, passado como
argumento para outra função ou utilizado diretamente em expressões.

O uso do `return` é fundamental para criar funções reutilizáveis, previsíveis
e que se comuniquem com o restante do programa por meio de seus resultados.
"""

# variavel = print('João')
# print(print('João'))
# print(variavel)
# print(variavel is None)

def soma(x, y):
    print(x + y)

def outra_soma(a, b):
    if a > 10:
        return 10, 20
    return a + b

resultado_soma = soma(1, 2)
resultado_outra_soma = outra_soma(1, 2)
print('Retorno da função soma():', resultado_soma)
print('Retorno da função outra_soma():', resultado_outra_soma)

soma1 = outra_soma(2, 2)
soma2 = outra_soma(3, 3)
print(f'{soma1} + {soma2} = {soma1 + soma2}')
print(outra_soma(11, 2))
