"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_str = input('Digite um número inteiro: ')

# Solução 01
# try:
#     numero_int = int(numero_str)
#     if numero_int % 2 == 0:
#         print(f'O número {numero_int} é par.')
#     else:
#         print(f'O número {numero_int} é ímpar.')
# except:
#     print('Você não digitou um número inteiro.')

# Solução 02
# if numero_str.isdigit():
#     numero_int = int(numero_str)
#     if numero_int % 2 == 0:
#         print(f'O número {numero_int} é par.')
#     else:
#         print(f'O número {numero_int} é ímpar.')
# else:
#     print('Você não digitou um número inteiro.')

# Solução 03
# if numero_str.isdigit():
#     numero_int = int(numero_str)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {numero_int} é {par_impar_texto}.')

# else:
#     print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. 
Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual_str = input('Digite a hora atual [0-23]: ')
hora_atual_int = None

# Solução 01
# try:
#     hora_atual_int = int(hora_atual_str)
#     if hora_atual_int >= 0 and hora_atual_int <= 11:
#         print('Bom dia!')
#     elif hora_atual_int >= 12 and hora_atual_int <= 17:
#         print('Boa tarde!')
#     elif hora_atual_int >= 18 and hora_atual_int <= 23:
#         print('Boa noite!')
#     else:
#         print('A hora informada não é válida.')
# except:
#     print('Você não digitou um número inteiro.')

# Solução 02
if hora_atual_str.isdigit():
    hora_atual_int = int(hora_atual_str)
    if hora_atual_int >= 0 and hora_atual_int <= 11:
        print('Bom dia!')
    elif hora_atual_int >= 12 and hora_atual_int <= 17:
        print('Boa tarde!')
    elif hora_atual_int >= 18 and hora_atual_int <= 23:
        print('Boa noite!')
    else:
        print('A hora informada não é válida.')
else:
    print('Você não digitou um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Solução 01
primeiro_nome = input('Digite o seu primeiro nome: ')
tamanho_do_primeiro_nome = len(primeiro_nome)
nome_curto = tamanho_do_primeiro_nome > 1 and tamanho_do_primeiro_nome <= 4
nome_normal = tamanho_do_primeiro_nome >= 5 and tamanho_do_primeiro_nome <= 6
nome_grande = tamanho_do_primeiro_nome > 6

if nome_curto:
    print('Seu nome é curto.')
elif nome_normal:
    print('Seu nome é normal.')
elif nome_grande:
    print('Seu nome é muito grande.')
else:
    print('O nome digitado é inválido e/ou nulo.')
