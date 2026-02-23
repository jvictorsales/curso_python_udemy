"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
lista_frases = frase.split(',')
print(lista_palavras)

lista_frases_corrigida = []
for i, frase in enumerate(lista_frases):
    lista_frases_corrigida.append(lista_frases[i].strip())

print(lista_frases)
print(lista_frases_corrigida)


# frases_unidas = '-'.join('abc')
# print(frases_unidas)

frases_unidas = ', '.join(lista_frases_corrigida)
print(frases_unidas)
