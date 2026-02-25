# Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


# # Minha solução
# def validar_opcao_escolhida(opcao_escolhida_str):
#     if opcao_escolhida_str.isdigit():
#         opcao_escolhida_int = int(opcao_escolhida_str)
#         return opcao_escolhida_int

# def verificar_opcao_correta(resposta_usuario, resposta_correta, pontuacao_atual):
#     if resposta_usuario == resposta_correta:
#         pontuacao_nova = pontuacao_atual + 1
#         return pontuacao_nova
#     return pontuacao_atual

# pontuacao_atual = 0
# qtd_perguntas = len(perguntas)

# for dicionario in perguntas:
#     pergunta = dicionario.get('Pergunta')
#     opcoes = dicionario.get('Opções')
#     resposta_correta = dicionario.get('Resposta')
    
#     print(f'Pergunta: {pergunta}')
#     print()

#     print('Opções:')
#     for indice, opcao in enumerate(opcoes):
#         print(f'{indice}) {opcao}')
#     print()

#     opcao_escolhida_str = input('Escolha uma opção: ')
#     opcao_validada = validar_opcao_escolhida(opcao_escolhida_str)
    
#     print()
#     if(opcao_validada) is None:
#         print('Errou!')
#     else:
#         resposta_usuario = opcoes[opcao_validada]
#         pontuacao_atual = verificar_opcao_correta(resposta_usuario, resposta_correta, pontuacao_atual)
#         print(f'Acertou {pontuacao_atual}/{qtd_perguntas} perguntas.')


# Solução do professor
qtd_acertos = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')
    print()

    print(f'Opções: ')
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
