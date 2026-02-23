"""
Introdução ao desempacotamento
"""

# nomes = ['Maria', 'Helena', 'João']
# nome_1, nome_2, nome_3 = nomes
# nome_1, nome_2, nome_3 = ['Maria', 'Helena', 'João']

# nome_1, *resto = ['Maria', 'Helena', 'João']
# print(nome_1, resto)

# nome_1, *_ = ['Maria', 'Helena', 'João']
# print(nome_1)

# _, nome_2, *_ = ['Maria', 'Helena', 'João']
# print(nome_2)

# _, _, nome_3, *_ = ['Maria', 'Helena', 'João']
# print(nome_3)

_, _, nome_3, *resto = ['Maria', 'Helena', 'João']
print(nome_3, resto)
