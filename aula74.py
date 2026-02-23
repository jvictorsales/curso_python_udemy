"""
Closure e funções que retornam outras funções

Em Python, funções são objetos de primeira classe. Isso significa que elas podem:
- Ser atribuídas a variáveis
- Ser passadas como argumentos
- Ser retornadas por outras funções

Uma função que retorna outra função é a base do conceito de closure.

--------------------------------------------------
O que é uma Closure?
--------------------------------------------------
Uma closure acontece quando:
1. Uma função interna (função aninhada) é definida dentro de outra função
2. A função interna utiliza variáveis da função externa
3. A função externa retorna a função interna
4. Mesmo após a função externa ter sido finalizada, a função interna
   continua tendo acesso às variáveis do escopo externo

Ou seja:
👉 A função "lembra" do ambiente onde foi criada.

--------------------------------------------------
Exemplo simples de função retornando outra função
--------------------------------------------------
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar


# Criando funções a partir da função externa
bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")

print(bom_dia("João"))      # Bom dia, João!
print(boa_noite("Maria"))  # Boa noite, Maria!


"""
--------------------------------------------------
Por que isso é uma Closure?
--------------------------------------------------
A função 'saudar':
- Usa a variável 'saudacao'
- 'saudacao' pertence ao escopo da função externa 'criar_saudacao'
- Mesmo após 'criar_saudacao' terminar, 'saudar' continua acessando
  o valor de 'saudacao'

Isso caracteriza uma closure.

--------------------------------------------------
Exemplo prático: função multiplicadora
--------------------------------------------------
"""

def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar


dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(10))   # 20
print(triplo(10))  # 30


"""
--------------------------------------------------
Aplicações comuns de Closures
--------------------------------------------------
- Criar funções configuráveis
- Evitar variáveis globais
- Encapsular lógica e estado
- Decorators (uso avançado de closures)
- Factory functions (funções fábrica)

--------------------------------------------------
Resumo
--------------------------------------------------
- Funções podem retornar outras funções
- Closures permitem que a função interna "lembre" do escopo externo
- São úteis para organização, reutilização e encapsulamento de código
- Muito usadas em programação funcional e em decorators
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar
    

s1 = criar_saudacao('Bom dia', 'João')
s2 = criar_saudacao('Boa noite', 'João')

print(s1())
print(s2())
