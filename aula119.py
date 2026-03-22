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
import json

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

# def salvar_dados(lista_de_tarefas, caminho_arquivo):
#     with open(caminho_arquivo, 'w', encoding='utf8') as file:
#         json.dump(lista_de_tarefas, file, indent=2, ensure_ascii=False)

# def carregar_dados(caminho_arquivo):
#     if os.path.exists(caminho_arquivo):
#         with open(caminho_arquivo) as file:
#             lista_de_tarefas = json.load(file)
#             return lista_de_tarefas
#     return []


def ler(lista_de_tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe.')
        salvar(lista_de_tarefas, caminho_arquivo)

    return dados

def salvar(lista_de_tarefas, caminho_arquivo):
    dados = lista_de_tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista_de_tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula119.json'
# lista_de_tarefas = carregar_dados(CAMINHO_ARQUIVO)
lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
lista_de_tarefas_removidas = []

while True:
    print()
    # print('Comandos: listar, desfazer, refazer, clear, salvar, sair')
    print('Comandos: listar, desfazer, refazer, clear, sair')
    tarefa = input('Digite uma tarefa ou comando: ').strip()
    
    # if tarefa == 'sair':
    #     print()
    #     print('Saindo...')
    #     print()
    #     break
    # elif tarefa == 'listar':
    #     exibir_tarefas(lista_de_tarefas)
    # elif tarefa == 'desfazer':
    #     defazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas)
    # elif tarefa == 'refazer':
    #     refazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas)
    # else:
    #     adicionar_tarefa(tarefa, lista_de_tarefas)

    if tarefa == 'sair':
        print()
        print('Saindo...')
        print()
        break

    comandos = {
        'listar': lambda: exibir_tarefas(lista_de_tarefas),
        'desfazer': lambda: defazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas),
        'refazer': lambda: refazer_tarefa(lista_de_tarefas, lista_de_tarefas_removidas),
        'clear': lambda: limpar_tela(),
        'adicionar': lambda: adicionar_tarefa(tarefa, lista_de_tarefas),
        # 'salvar': lambda: salvar_dados(lista_de_tarefas, CAMINHO_ARQUIVO)
    }

    comando = comandos.get(tarefa, comandos['adicionar'])
    comando()
    salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
