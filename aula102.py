"""
Variáveis livres, nonlocal, global, locals() e globals() em Python

Python utiliza um sistema de escopos para determinar onde as variáveis
são criadas, acessadas e modificadas. Esse sistema segue a regra chamada:

LEGB Rule

L → Local
E → Enclosing
G → Global
B → Built-in

A ordem acima representa a forma como o Python procura uma variável.

---

1. ESCOPO LOCAL

---

O escopo local corresponde às variáveis criadas dentro de uma função.

Exemplo:

def funcao():
    x = 10
    print(x)

funcao()

Neste caso:
x é uma variável LOCAL da função.

---

2. ESCOPO GLOBAL

---

O escopo global corresponde às variáveis definidas no nível do módulo
(ou seja, fora de funções).

Exemplo:

x = 10

def funcao():
    print(x)

funcao()

Aqui a função consegue acessar x porque ele está no escopo global.

---

3. VARIÁVEIS LIVRES (FREE VARIABLES)

---

Uma variável livre é uma variável utilizada dentro de uma função
interna, mas que foi definida em uma função externa.

Exemplo:

def externa():
    x = 10

    def interna():
        print(x)

    interna()


Nesse caso:

* x NÃO é local da função interna
* x pertence à função externa

Portanto, x é considerada uma VARIÁVEL LIVRE dentro de "interna".

---

4. PROBLEMA AO MODIFICAR VARIÁVEIS LIVRES

---

Se tentarmos modificar uma variável livre diretamente, ocorrerá erro.

Exemplo:

def externa():
    x = 10

    def interna():
        x = x + 1
        print(x)

    interna()


Erro: UnboundLocalError

Isso acontece porque o Python entende que x é uma variável local
da função interna, mas ela está sendo utilizada antes de ser criada.

---

5. NONLOCAL

---

A palavra-chave "nonlocal" permite modificar uma variável que pertence
ao escopo de uma função externa.

Exemplo:

def externa():
    x = 10

    def interna():
        nonlocal x
        x += 1
        print(x)

    interna()
externa()

Saída: 11

Agora o Python entende que x pertence à função externa.

---

6. GLOBAL

---

A palavra-chave "global" permite modificar uma variável do escopo global.

Exemplo:

x = 10

def funcao():
    global x
    x = 20

funcao()
print(x)

Saída: 20

---

7. DIFERENÇA ENTRE GLOBAL E NONLOCAL

---

global
→ modifica variáveis definidas no escopo global

nonlocal
→ modifica variáveis definidas em funções externas

Estrutura visual:

GLOBAL
|
função_externa()
|
função_interna()

* nonlocal sobe um nível (função externa)
* global sobe até o escopo do módulo

---

8. LOCALS()

---

A função locals() retorna um dicionário contendo todas as variáveis
do escopo local atual.

Exemplo:

def funcao():
    x = 10
    y = 20
    print(locals())

funcao()

Saída: {'x': 10, 'y': 20}

---

9. GLOBALS()

---

A função globals() retorna um dicionário contendo todas as variáveis
globais do módulo.

Exemplo:

x = 10

print(globals())

---

10. RELAÇÃO COM CLOSURES

---

Quando uma função interna acessa variáveis livres, o Python cria
uma estrutura chamada CLOSURE.

Essa estrutura permite que a função interna "lembre" das variáveis
da função externa mesmo depois que ela termina de executar.

Exemplo:

def criar_contador():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador

    return incrementar


contador = criar_contador()

print(contador())
print(contador())
print(contador())

Saída:

1
2
3

O valor de "contador" continua existindo graças ao mecanismo
de closure do Python.

---

## RESUMO

locals()
→ retorna variáveis do escopo local

globals()
→ retorna variáveis do escopo global

global
→ permite modificar variáveis globais

nonlocal
→ permite modificar variáveis de uma função externa

variável livre
→ variável usada em uma função, mas definida em um escopo externo
"""


# print(globals())

# def fora(x):
#     a = x
#     def dentro():
#         # print(locals())
#         # print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar        
        return valor_final
    
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c()
print(final)
