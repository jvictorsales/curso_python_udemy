palavra_secreta = 'fevereiro'
tamanho_palavra_secreta = len(palavra_secreta)
chute_letra = ''
letras_chutadas = ''
palavra_chutada = '*' * tamanho_palavra_secreta
letras_permitidas = 'abcdefghijklmnopqrstuvwxyz'
vidas = 6

print('Jogo da Forca - Advinhe a palavra Secreta')
print(f'A palavra secreta tem {palavra_chutada} ({tamanho_palavra_secreta} letras)')

while True:

    if palavra_chutada == palavra_secreta:
        print(f'Você encontrou a palavra secreta: {palavra_secreta}')
        break

    chute_letra = input('Digite uma letra: ')

    if chute_letra not in letras_permitidas:
        print('Digite apenas letras permitidas: (a-z)')
        continue

    if chute_letra == '':
        print('Você não digitou nada, tente novamente.')
        continue

    if chute_letra in letras_chutadas:
        print('Letra já foi chutada, tente outra letra.')
        continue

    if chute_letra not in palavra_secreta:
        vidas -= 1
        print('Perdeu -1 vida')
        print(f'Restam: {vidas} vidas')

    if vidas == 0:
        print(f'Você perdeu!')
        break

    letras_chutadas += chute_letra

    palavra_chutada_temporaria = ''
    for i in range(tamanho_palavra_secreta):
        if palavra_secreta[i] == chute_letra: 
            palavra_chutada_temporaria += chute_letra
        else:
            palavra_chutada_temporaria += palavra_chutada[i]

    palavra_chutada = palavra_chutada_temporaria

    print(f'Palavra chutada: {palavra_chutada}')
    print(f'Letras já chutadas: {letras_chutadas}')


# import os

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')

#     if len(letra_digitada) > 1:
#         print('Digite apenas 1 letra.')
#         continue

#     numero_tentativas += 1

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada
    
#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'
    
#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('cls')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0
