"""
Higher-Order Functions (Funções de Ordem Superior)

Em Python, uma Higher-Order Function é uma função que atende
a pelo menos um dos seguintes critérios:

1. Recebe uma ou mais funções como argumento
2. Retorna uma função como resultado

Isso é possível porque, em Python, funções são objetos de
primeira classe (first-class citizens), ou seja:
- Podem ser atribuídas a variáveis
- Podem ser passadas como argumento
- Podem ser retornadas por outras funções

----------------------------------------
Funções como argumento
----------------------------------------
Uma função pode receber outra função para decidir
como um determinado comportamento será executado.

Exemplo clássico:
- map()
- filter()
- sorted()
- funções customizadas que recebem callbacks

----------------------------------------
Funções que retornam funções
----------------------------------------
Uma função pode criar e retornar outra função,
permitindo comportamentos dinâmicos, encapsulamento
de lógica e reutilização de código.

Esse conceito é muito usado em:
- Closures
- Decorators
- Programação funcional

----------------------------------------
Vantagens das Higher-Order Functions
----------------------------------------
- Código mais reutilizável
- Menor duplicação de lógica
- Maior flexibilidade
- Funções mais genéricas e expressivas

----------------------------------------
Resumo
----------------------------------------
Higher-Order Functions permitem tratar funções como dados,
possibilitando composições mais poderosas e elegantes
no desenvolvimento em Python.
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

# saudacao_2 = saudacao
# v = executa(saudacao, 'Bom dia', 'João')
print(
    executa(saudacao, 'Bom dia', 'João')
)
print(
    executa(saudacao, 'Boa Noite', 'Maria')
)
# v = saudacao('Bom dia')
# v = saudacao_2('Bom dia')


"""
First-Class Functions (Funções de Primeira Classe)

Em Python, dizemos que funções são First-Class Functions
(funções de primeira classe) porque elas são tratadas
como qualquer outro objeto da linguagem.

Isso significa que funções podem:

1. Ser atribuídas a variáveis
2. Ser passadas como argumento para outras funções
3. Ser retornadas por outras funções
4. Ser armazenadas em estruturas de dados (listas, dicionários, etc.)

----------------------------------------
Atribuição de funções a variáveis
----------------------------------------
Uma função pode ser atribuída a uma variável
sem ser executada (sem parênteses).

Exemplo conceitual:
- func = minha_funcao
- func() executa a função referenciada

----------------------------------------
Funções como argumento
----------------------------------------
Uma função pode ser passada como argumento
para outra função, permitindo comportamentos
personalizáveis e reutilizáveis.

Esse conceito é a base para:
- Callbacks
- Higher-Order Functions

----------------------------------------
Funções como retorno
----------------------------------------
Uma função pode criar e retornar outra função,
permitindo encapsular lógica e criar comportamentos
dinâmicos.

Esse conceito é muito utilizado em:
- Closures
- Decorators

----------------------------------------
Funções em estruturas de dados
----------------------------------------
Funções podem ser armazenadas em listas,
tuplas ou dicionários e chamadas dinamicamente.

----------------------------------------
Resumo
----------------------------------------
First-Class Functions são o fundamento que
torna possível a programação funcional em Python.
Sem esse conceito, Higher-Order Functions,
closures e decorators não existiriam.
"""