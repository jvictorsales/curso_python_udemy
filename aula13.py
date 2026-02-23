nome = 'João Victor'
altura = 1.75
peso = 85
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura} de altura,\n'
linha_2 = f'pesa {peso} quilos e seu IMC é\n'
linha_3 = f'{imc:.2f}'
texto = linha_1 + linha_2 + linha_3
print(texto)

# João Victor tem 1.75 de altura,
# pesa 85 quilos e seu IMC é
# 27.755102040816325
