# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# import os

# def adicionar_tarefa():
#     tarefa = input('Tarefa: ')
#     lista_de_tarefas.append(tarefa)
#     limpar_tela()
    
# def desfazer_tarefa():
#     limpar_tela()
#     if lista_de_tarefas:
#         lista_de_tarefas_removidas.append(lista_de_tarefas[-1])
#         lista_de_tarefas.pop()
#         return
    
#     print('Nenhuma tarefa para desfazer.')
#     return
    
# def refazer_tarefa():
#     limpar_tela()
#     if lista_de_tarefas_removidas:
#         lista_de_tarefas.append(lista_de_tarefas_removidas[-1])
#         lista_de_tarefas_removidas.pop()
#         return
    
#     print('Nenhuma tarefa para refazer.')
#     return
    
# def exibir_lista_de_tarefas(lista_de_tarefas):
#     print()
#     print('--- LISTA DE TAREFAS ---')
#     if lista_de_tarefas:
#         for tarefa in lista_de_tarefas:
#             print(f'- {tarefa}')

# def exibir_menu():
#     print()
#     print('1 - Adicionar tarefa')
#     print('2 - Desfazer tarefa')
#     print('3 - Refazer tarefa')
#     print('0 - Sair')
#     print()

# def limpar_tela():
#     os.system('cls')

# lista_de_tarefas = []
# lista_de_tarefas_removidas = []

# while True:

#     exibir_menu()

#     opcao_usuario = input('Escolha uma opção: ')
    
#     if opcao_usuario.isdigit():
#         opcao_usuario = int(opcao_usuario)
#     else:
#         limpar_tela()
#         print('Opção inválida, tente novamente.')
#         continue

#     if opcao_usuario == 0:
#         print()
#         print('Saindo...')
#         print()
#         break
#     elif opcao_usuario == 1:
#         adicionar_tarefa()
#         exibir_lista_de_tarefas(lista_de_tarefas)
#     elif opcao_usuario == 2:
#         desfazer_tarefa()
#         exibir_lista_de_tarefas(lista_de_tarefas)
#     elif opcao_usuario == 3:
#         refazer_tarefa()
#         exibir_lista_de_tarefas(lista_de_tarefas)
#     else:
#         limpar_tela()
#         print('Opção inexistente, tente novamente.')
#         continue


import os

def limpar_tela():
    os.system('cls')

def adicionar_tarefa(tarefa, lista_de_tarefas):   
    if tarefa in lista_de_tarefas:
        print()
        print('Tarefa já foi adicionada.')
        return

    if tarefa == '':
        print()
        print('Nenhuma tarefa digitada.')
        return

    lista_de_tarefas.append(tarefa)
    exibir_tarefas(lista_de_tarefas)

def defazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas):
    if not lista_de_tarefas:
        print()
        print('Nada para desfazer.')
        return
    
    tarefa  = lista_de_tarefas.pop()
    lista_de_tarefas_removidas.append(tarefa)
    exibir_tarefas(lista_de_tarefas)

def refazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas):
    if not lista_de_tarefas_removidas:
        print()
        print('Nada para refazer.')
        return
    
    tarefa = lista_de_tarefas_removidas.pop()
    lista_de_tarefas.append(tarefa)
    exibir_tarefas(lista_de_tarefas)

def exibir_tarefas(lista_de_tarefas):
    limpar_tela()

    if not lista_de_tarefas:
        print('Nenhuma tarefa para exibir.')
        return
    
    print()
    print('=== LISTA DE TAREFAS ===')
    for tarefa in lista_de_tarefas:
        print(f'\t- {tarefa}')
    print()

lista_de_tarefas = []
lista_de_tarefas_removidas = []

while True:
    print()
    print('Comandos: listar, desfazer, refazer, sair')
    tarefa = input('Digite uma tarefa ou comando: ').strip()
    
    if tarefa == 'sair':
        print()
        print('Saindo...')
        print()
        break
    elif tarefa == 'listar':
        exibir_tarefas(lista_de_tarefas)
    elif tarefa == 'desfazer':
        defazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas)
    elif tarefa == 'refazer':
        refazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas)
    else:
        adicionar_tarefa(tarefa, lista_de_tarefas)
