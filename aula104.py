"""
Decoradores com Parâmetros em Python
====================================

Decoradores com parâmetros são uma extensão dos decorators tradicionais.
Eles permitem configurar o comportamento do decorator através de argumentos.

Para que isso funcione, é necessário adicionar um nível extra de função,
criando uma "fábrica de decoradores".

---------------------------------------------------------------------

Estrutura conceitual
--------------------

Um decorator simples possui duas funções:

    decorador(func)
        wrapper(*args, **kwargs)

Já um decorator com parâmetros possui três níveis:

    fabrica_de_decoradores(parametros)
        decorador(func)
            wrapper(*args, **kwargs)

Cada função tem uma responsabilidade diferente:

1) Função externa (fábrica)
   Recebe os parâmetros do decorator.

2) Função decoradora
   Recebe a função que será decorada.

3) Função wrapper (aninhada)
   Executa código antes/depois da função original.


---------------------------------------------------------------------

Fluxo de execução
-----------------

Quando Python encontra a sintaxe:

    @decorador(a, b, c)
    def funcao():
        pass

Ele transforma isso em:

    funcao = decorador(a, b, c)(funcao)

Ou seja, primeiro o decorator é chamado com os parâmetros,
depois a função resultante recebe a função original.

Fluxo completo:

    decorador(a, b, c)
            ↓
    retorna funcao_decoradora
            ↓
    funcao_decoradora(funcao_original)
            ↓
    retorna wrapper
            ↓
    funcao_original passa a apontar para wrapper


---------------------------------------------------------------------

Exemplo de implementação
------------------------

    def fabrica_de_decoradores(a, b, c):

        def decorador(func):

            def wrapper(*args, **kwargs):
                print('Parâmetros do decorator:', a, b, c)

                resultado = func(*args, **kwargs)

                return resultado

            return wrapper

        return decorador


Uso:

    @fabrica_de_decoradores(1, 2, 3)
    def soma(x, y):
        return x + y


---------------------------------------------------------------------

Ordem das execuções
-------------------

1) O decorator é executado quando o módulo é carregado
2) A função decorada é substituída pela função wrapper
3) Quando a função é chamada, quem executa é o wrapper

Ou seja:

    definição da função → aplicação do decorator
    chamada da função → execução do wrapper


---------------------------------------------------------------------

Relação com closures
--------------------

Decoradores funcionam graças ao conceito de closures.

A função wrapper mantém acesso às variáveis do escopo externo,
como os parâmetros do decorator e a função original.

Exemplo de variáveis capturadas:

    a, b, c   → parâmetros do decorator
    func      → função original


---------------------------------------------------------------------

Uso comum na prática
--------------------

Decoradores com parâmetros são usados quando queremos
configurar o comportamento do decorator.

Exemplos comuns:

• Sistemas de permissão
• Logging configurável
• Controle de tentativas (retry)
• Validação de parâmetros
• Cache configurável
• Medição de performance
• Frameworks web (Flask, Django, FastAPI)


---------------------------------------------------------------------

Resumo
------

Decorator simples:

    @decorador
    def func():
        pass

Equivalente a:

    func = decorador(func)


Decorator com parâmetros:

    @decorador(a, b, c)
    def func():
        pass

Equivalente a:

    func = decorador(a, b, c)(func)

Portanto, decorators com parâmetros são essencialmente
"funções que retornam decorators".
"""

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmentros do decorador:', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

# def fabrica_de_decoradores(a, b, c):
#     return fabrica_de_funcoes

# def blablabla(a, b, c):
#     print(a, b, c)
#     return decoradora


# @blablabla(1, 2, 3)
# @fabrica_de_funcoes
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
