"""
Operadores lógicos e avaliação de curto-circuito em Python.

Operadores lógicos são usados para combinar ou inverter expressões booleanas
(True ou False). Em Python, os principais operadores lógicos são:

- and (e)
- or (ou)
- not (não)

1) Operador `and`
O operador `and` retorna True somente se **todas** as condições envolvidas
forem verdadeiras. Caso qualquer uma delas seja considerada falsa (falsy),
a expressão inteira será avaliada imediatamente como falsa.

Além disso, o `and` não retorna necessariamente True ou False: ele retorna
o primeiro valor falsy encontrado ou o último valor avaliado, se todos
forem truthy.

Exemplos de valores considerados falsy em Python:
- 0
- 0.0
- ''
- False
- None

2) Operador `or`
O operador `or` retorna True se **pelo menos uma** das condições for verdadeira.
Assim como o `and`, ele não retorna apenas valores booleanos: o `or` retorna
o primeiro valor truthy encontrado ou o último valor avaliado, caso todos
sejam falsy.

3) Operador `not`
O operador `not` inverte o valor lógico de uma expressão:
- True se torna False
- False se torna True

4) None
O valor `None` representa a ausência de valor (um “não valor”). Ele é
avaliado como falsy em expressões lógicas e é comumente usado para indicar
que algo ainda não foi definido ou retornado.

Avaliação de curto-circuito (short-circuit evaluation):

A avaliação de curto-circuito ocorre quando o Python interrompe a análise
de uma expressão lógica assim que o resultado final já pode ser determinado.

- No `and`: se uma condição for falsy, as próximas não são avaliadas,
  pois o resultado final já será falso.
- No `or`: se uma condição for truthy, as próximas não são avaliadas,
  pois o resultado final já será verdadeiro.

Esse comportamento melhora a performance e também evita erros, como acessar
variáveis, funções ou operações que não deveriam ser executadas em certas
condições.
"""


# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Informe sua senha: ')
# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(0 or False or 0 or 'abc' or True)
# senha = input('Senha: ') or 'Sem senha'
