"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

# contador = 0
# while contador <= 10:
#     print(contador)
#     contador += 1


# Loop infinito -> Quando um código não tem fim
# condicao = True
# while condicao:
#     print(1)
#     print(2)
#     print(3)

condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')