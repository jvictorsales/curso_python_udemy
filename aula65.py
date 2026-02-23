"""
Introdução às Funções (def) em Python

Funções são blocos de código reutilizáveis criados para executar
uma tarefa específica dentro de um programa. Seu principal objetivo
é evitar repetição de código, melhorar a organização e aumentar
a legibilidade da aplicação.

Em Python, funções são definidas utilizando a palavra-chave `def`,
seguida pelo nome da função, parênteses e dois pontos. O código
pertencente à função deve estar indentado.

Uma função pode receber dados de entrada por meio de parâmetros,
que são variáveis declaradas na definição da função. Quando a função
é chamada, os valores fornecidos a esses parâmetros são chamados
de argumentos.

Funções podem ou não retornar valores. O retorno é feito através
da palavra-chave `return`. Caso nenhuma instrução `return` seja
definida, a função retornará automaticamente o valor `None`.

O uso de funções permite dividir problemas complexos em partes
menores, facilitando a manutenção, reutilização e testes do código.

Resumo dos conceitos:
- Parâmetros: variáveis definidas na declaração da função
- Argumentos: valores passados para a função no momento da chamada
- Retorno: valor devolvido pela função ao final de sua execução
"""

def cumprimentar_usuario(nome='Fulano'):  # nome é o parâmetro
    print(f'Olá {nome}, seja bem-vindo!')

cumprimentar_usuario('João')  # 'João' é o argumento
cumprimentar_usuario('Ruth')
cumprimentar_usuario('Maria')
cumprimentar_usuario('Helena')
cumprimentar_usuario()
