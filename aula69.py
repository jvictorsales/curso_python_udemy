"""
Escopo de funções em Python

Escopo define onde um nome (variável, função, objeto) pode ser acessado
dentro de um programa.

Em Python, os nomes não são visíveis em todo o código automaticamente;
eles pertencem a um escopo específico.

Tipos principais de escopo:

1) Escopo Global
   - É o escopo do módulo (arquivo).
   - Tudo que é definido fora de funções e classes pertence a esse escopo.
   - Variáveis globais podem ser lidas dentro de funções.

   Exemplo:
       x = 10

       def funcao():
           print(x)  # acesso ao escopo global

2) Escopo Local
   - É o escopo criado dentro de uma função.
   - Variáveis definidas dentro de uma função só existem nela.
   - Ao final da execução da função, o escopo local é destruído.

   Exemplo:
       def funcao():
           y = 5  # variável local
           print(y)

       funcao()
       # print(y)  # erro: y não existe fora da função

3) Leitura vs Modificação de variáveis globais
   - Uma função pode ler uma variável global.
   - Para modificar uma variável global, é necessário usar a palavra-chave 'global'.
   - Sem 'global', uma atribuição cria uma nova variável local.

   Exemplo:
       x = 10

       def funcao():
           x = 20  # cria variável local

       funcao()
       print(x)  # continua sendo 10

4) Palavra-chave 'global'
   - Indica explicitamente que a variável pertence ao escopo global.
   - Seu uso é desencorajado em código profissional, pois aumenta o acoplamento
     e dificulta manutenção.

   Exemplo:
       x = 10

       def funcao():
           global x
           x = 20

5) Escopos Aninhados
   - Funções internas conseguem acessar variáveis das funções externas.
   - Funções externas não conseguem acessar variáveis das internas.

   Exemplo:
       def externa():
           a = 10

           def interna():
               print(a)

           interna()

6) Regra LEGB (ordem de busca de nomes)
   - L: Local
   - E: Enclosing (funções externas)
   - G: Global
   - B: Built-in (funções nativas como print, len, int)

   O Python procura um nome nessa ordem até encontrá-lo.

Resumo:
- Escopo global: visível em todo o módulo.
- Escopo local: visível apenas dentro da função.
- Variáveis locais não vazam para fora da função.
- Evite o uso de 'global'; prefira retornar valores.
"""

x = 1

def escopo():
    # global x
    x = 10

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)


"""
Call Stack (Pilha de Chamadas)

A call stack é uma estrutura de dados do tipo pilha (LIFO – Last In, First Out)
utilizada pelo interpretador Python para controlar a execução das funções
durante a execução de um programa.

Sempre que uma função é chamada, o Python cria um frame de execução
(quadro de pilha) contendo informações como:
- Variáveis locais da função
- Parâmetros recebidos
- O ponto do código para onde a execução deve retornar
- Referência ao escopo anterior

Esse frame é empilhado na call stack. Quando a função finaliza sua execução,
seu frame é removido da pilha, e o controle do programa retorna para a função
que realizou a chamada.

A call stack permite que o Python saiba exatamente qual função está sendo
executada no momento e em qual ordem as funções foram chamadas, garantindo
o fluxo correto do programa e o funcionamento adequado do comando `return`.

Em chamadas recursivas, cada invocação da função cria um novo frame na call
stack. Caso a profundidade de chamadas ultrapasse o limite permitido pelo
Python, ocorre um erro do tipo `RecursionError`, indicando estouro da pilha.

Os tracebacks exibidos em erros de execução representam o estado da call
stack no momento da falha, mostrando a sequência de chamadas que levou
ao erro.
"""

print()

def f(n):
    if n == 0:
        return

    f(n - 1)
    print(n)

f(10)
print('Fim da func')

print()


lista = [1, 2, 3, 4, 5]
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_lista(lista[1:])

resultado_soma_lista = soma_lista(lista)
print(resultado_soma_lista)

print()

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

resultado_fatorial = fatorial(3)
print(resultado_fatorial)