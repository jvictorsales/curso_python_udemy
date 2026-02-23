frase = 'O python é uma linguagem de programação ' \
        'multiparadigma.' \
        'Python foi criado por Guido Van Rossum.'

# tamanho_frase = len(frase)
# letras_checadas = ''
# i = 0

# while i < tamanho_frase:
#     letra_atual = frase[i]
    
#     if letra_atual == ' ':
#         i += 1
#         continue

#     if letra_atual in letras_checadas:
#         i += 1
#         continue

#     j = 0
#     contador = 0
#     while j < tamanho_frase:
#         if letra_atual == frase[j]:
#             contador += 1
#         j += 1
    
#     letras_checadas += letra_atual

#     print(f'A letra {letra_atual} apareceu {contador} vez(es).')

#     i += 1


i = 0
tamanho_frase = len(frase)
qtd_nova_letra_apareceu = 0
nova_letra_mais_repetida = ''

while i < tamanho_frase:
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual_apareceu = frase.count(letra_atual)

    if qtd_letra_atual_apareceu > qtd_nova_letra_apareceu:
        qtd_nova_letra_apareceu = qtd_letra_atual_apareceu
        nova_letra_mais_repetida = letra_atual
    
    i += 1

print(f'A letra que mais apareceu foi: "{nova_letra_mais_repetida}" = {qtd_nova_letra_apareceu} vez(es)')
