"""
Mapeamento de dados em List Comprehension

Mapeamento significa transformar cada elemento de um iterável
em outro valor. Em Python, fazemos isso aplicando uma expressão
a cada item dentro da list comprehension.

Em termos simples:

    "Para cada item, gere um novo valor."

------------------------------------------------------------

Estrutura do mapeamento:

    [transformação for item in iterável]

A parte antes do "for" é a transformação (o mapeamento).
Ela é aplicada a cada elemento.
"""

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


print('Exemplo 1 — Dobrar valores')

numeros = [1, 2, 3, 4]
dobro = [n * 2 for n in numeros]
print(numeros)
print(dobro)

# Aqui:
# - n é o item atual
# - n * 2 é o mapeamento
# - resultado: [2, 4, 6, 8]

print()
print('Exemplo 2 — Converter para string')

numeros = [10, 20, 30]
textos = [str(n) for n in numeros]
print(numeros)
print(textos)

print()
print('Exemplo 3 — Aplicar método')

nomes = ['joão', 'maria', 'ana']
maiusculos = [nome.upper() for nome in nomes]
print(nomes)
print(maiusculos)

print()
print('Exemplo 4 — Trabalhando com dicionários')

pessoas = [
    {'nome': 'João', 'idade': 20},
    {'nome': 'Maria', 'idade': 30}
]

idades = [p['idade'] for p in pessoas]

p(pessoas)
print('idades:', idades)

print()
print('Mapeamento + Condição')
print('Também podemos mapear apenas alguns elementos:')

numeros = [1, 2, 3, 4, 5]
quadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(numeros)
print(quadrados_pares)

# Aqui ocorre:
# - Filtro (if)
# - Mapeamento (n**2)


# Diferença mental importante:
# Mapear  = Transformar todos os elementos
# Filtrar = Escolher alguns elementos
# Mapear + Filtrar = Transformar apenas alguns

# Comparação com map():

# List comprehension:
[n * 2 for n in numeros]

# map():
list(map(lambda n: n * 2, numeros))

# A list comprehension é geralmente:
# - Mais legível
# - Mais usada em código moderno Python

# Resumo:
# Mapeamento em list comprehension é a parte da expressão
# que transforma cada elemento do iterável em um novo valor,
# gerando uma nova lista como resultado.


print()
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']} for produto in produtos
]

print('Produtos:')
p(produtos)

print()

print('Novos produtos:')
p(novos_produtos)


print()
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')
p(novos_produtos)

print()
lista = [n for n in range(10) if n < 5]
print(lista)

print()
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos)
