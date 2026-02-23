"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista_de_compras = []
opcoes_menu_permitidas = 'ials'

print('-- LISTA DE COMPRAS --')
print()

while True:
    print('Selecione uma opção')
    opcao_menu = input('[i]nser [a]pagar [l]istar [s]air: ').strip().lower()
    
    if opcao_menu not in opcoes_menu_permitidas:
        print('Opção inválida, tente novamente.')
        continue
    
    if opcao_menu == '':
        print('Escolha uma opção do menu e tente novamente.')
        continue

    if len(opcao_menu) > 1:
        print('Opção inválida, digite apenas 1 letra por vez.')
        continue

    if opcao_menu == 'i':
        os.system('cls')
        nome_item_da_lista_str = input('Nome do item: ').upper()

        if nome_item_da_lista_str == '':
            print('Nome não pode ser vazio.')
            continue

        lista_de_compras.append(nome_item_da_lista_str)
        print(f'{nome_item_da_lista_str} adicionado na lista.')

    elif opcao_menu == 'l':
        os.system('cls')
        if not lista_de_compras:
            print('Sua lista de compras está vazia, adicione novos items.')
            continue

        print('Exibindo sua Lista de Compras')
        for indice, nome_do_item in enumerate(lista_de_compras):
            print(f'- {indice} {nome_do_item}')

    elif opcao_menu == 'a':
        if not lista_de_compras:
            os.system('cls')
            print('Sua lista de compras está vazia.')
            continue

        # item_para_apagar = input('Digite o nome do item que deseja apagar: ').upper()

        indice_para_apagar_str = input('Digite o indice do item para apagar: ')

        try:
            indice_para_apagar_int = int(indice_para_apagar_str)
        except:
            print('Indice inválido.')
            continue
        
        os.system('cls')
        if (indice_para_apagar_int >= len(lista_de_compras)) or (indice_para_apagar_int < 0):
            print('Não foi possível apagar este índice.')
            continue
        
        print(f'{lista_de_compras[indice_para_apagar_int]} removido da sua lista.')
        lista_de_compras.pop(indice_para_apagar_int)

        # item_removido = False
        # for item_da_lista in lista_de_compras:
        #     if item_da_lista == item_para_apagar:
        #         lista_de_compras.remove(item_da_lista)
        #         item_removido = True

        # if item_removido:
        #     print('Item removido da sua lista.')
        # else:
        #     print('Item não encontrado na sua lista.')

    elif opcao_menu == 's':
        os.system('cls')
        print('Saindo...')
        break

    else:
        print('Você não deveria ter chegado aqui.')
        break
