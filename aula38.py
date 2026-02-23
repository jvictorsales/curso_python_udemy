"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linha = 5
qtd_coluna = 5

linha =  1

while linha <= qtd_linha:
    coluna = 1
    while coluna <= qtd_coluna:
        print(f'({linha},{coluna})', end= ' ')
        coluna += 1
    print()
    linha += 1

print('Acabou')
