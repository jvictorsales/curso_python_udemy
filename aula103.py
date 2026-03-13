# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

"""
Decorators (Funções Decoradoras) em Python
==========================================

Decorators são uma forma de modificar ou estender o comportamento de funções
ou métodos sem alterar diretamente o código da função original.

O termo "decorar" significa envolver uma função com outra função que irá
executar algum comportamento adicional antes, depois ou ao redor da função
original.

---------------------------------------------------------------------

Conceito principal
------------------

Uma função decoradora é uma função que:

1) Recebe outra função como argumento
2) Cria uma função interna (wrapper)
3) Executa código adicional
4) Chama a função original
5) Retorna a função interna

Estrutura básica:

    def decorador(func):
        def wrapper(*args, **kwargs):
            # comportamento antes
            resultado = func(*args, **kwargs)
            # comportamento depois
            return resultado
        return wrapper


---------------------------------------------------------------------

Sintaxe de uso com @
--------------------

Python fornece uma sintaxe especial chamada "decorator syntax":

    @decorador
    def minha_funcao():
        pass

Isso é equivalente a:

    def minha_funcao():
        pass

    minha_funcao = decorador(minha_funcao)

Ou seja, a função original é passada para o decorator e substituída
pela função retornada por ele.


---------------------------------------------------------------------

Função Wrapper
--------------

A função interna (geralmente chamada de wrapper) é responsável por:

- interceptar a chamada da função
- executar código adicional
- chamar a função original
- retornar o resultado

Por isso geralmente utilizamos:

    *args
    **kwargs

Para garantir que o decorator funcione com qualquer assinatura de função.


---------------------------------------------------------------------

Relação com outros conceitos do Python
--------------------------------------

Decorators dependem diretamente de vários conceitos importantes:

• First-Class Functions
  Funções podem ser tratadas como objetos.

• Higher-Order Functions
  Funções que recebem ou retornam outras funções.

• Closures
  A função interna mantém acesso às variáveis do escopo externo.

• Escopo Léxico
  A função wrapper consegue acessar a função original mesmo após
  o término da execução da função decoradora.


---------------------------------------------------------------------

Usos comuns de decorators
-------------------------

Decorators são muito usados para:

• Logging (registrar execução de funções)
• Medir tempo de execução
• Controle de acesso / autenticação
• Validação de dados
• Cache de resultados
• Retry automático
• Controle de permissões
• Frameworks web (Flask, Django, FastAPI)


Exemplo:

    def log_execucao(func):

        def wrapper(*args, **kwargs):
            print(f'Executando {func.__name__}')
            return func(*args, **kwargs)

        return wrapper


    @log_execucao
    def soma(a, b):
        return a + b


---------------------------------------------------------------------

Observação importante
---------------------

Quando usamos decorators, a função original é substituída pela função
wrapper retornada pelo decorator.

Por isso, para preservar metadados da função original (nome, docstring),
é comum usar:

    functools.wraps


---------------------------------------------------------------------

Resumo
------

Decorator = função que recebe uma função e retorna outra função.

    decorador(funcao) -> nova_funcao

A sintaxe com @ é apenas açúcar sintático para essa operação.

    @decorador
    def funcao():
        pass
"""

def criar_funcao(func):
    def interna(*args, **kwargs): 
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        # resultado += ' Qualquer Coisa'
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def is_string(param):
    print(f'{is_string.__name__}')
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('João')
invertida = inverte_string('João')
print(invertida)
