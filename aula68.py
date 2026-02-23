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
    global x
    x = 10
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
