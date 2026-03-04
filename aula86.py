# Dictionary Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    # if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

print(dc)

print()

lista_de_tuplas = [
    ('nome', 'Caneta Vermelha'),
    ('preco', 2.5),
    ('categoria', 'Escritório'),
]

dc = {
    chave: valor
    for chave, valor 
    in lista_de_tuplas
}
print(dc)
print(dict(lista_de_tuplas))

print()

numeros = [1, 2, 3, 4]
quadrados = {}

for n in numeros:
    quadrados[n] = n ** 2

print(quadrados)

print()

numeros = [1, 2, 3, 4]
quadrados = {n: n ** 2 for n in numeros}
print(quadrados)

print()

numeros = range(10)
pares = {n: n for n in numeros if n % 2 == 0}
par_ou_impar = {n: 'par' if n % 2 == 0 else 'ímpar' for n in numeros}
print(pares)
print(par_ou_impar)

print()

nomes = ['Ana', 'João', 'Maria']
tamanhos = {nome: len(nome) for nome in nomes}
print(tamanhos)

print()

d = {'a': 1, 'b': 2, 'c': 3}
invertido = {valor: chave for chave, valor in d.items()}
print(d)
print(invertido)

print()

# Atenção: Se houver valores repetidos, você perde dados (porque chaves não podem se repetir).
d = {'a': 1, 'b': 1, 'c': 3}
invertido = {valor: chave for chave, valor in d.items()}
print(d)
print(invertido)

print()

# Set Comprehension
numeros = [1, 2, 2, 3, 4]
quadrados = {n ** 2 for n in numeros}
print(quadrados)

print()

palavra = 'programação'
letras_unicas = {letra for letra in palavra}
print(letras_unicas)

print()

numeros = range(20)
impares = {n for n in numeros if n % 2 != 0}
print(impares)
