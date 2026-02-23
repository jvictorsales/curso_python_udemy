"""
Iterando strings com while
"""

#       012345678910
nome = 'João Victor'  # Iteráveis
#    -1110987654321

# print(nome)
# print(tamanho_nome)
# print(nome[5])

indice = 0
tamanho_nome = len(nome)
nova_string = ''

while indice < tamanho_nome:
    letra = nome[indice]
    nova_string += f'*{letra}'
    indice += 1

nova_string += '*'
print(nova_string)
