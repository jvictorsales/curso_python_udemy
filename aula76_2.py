# Manipulando chaves e valores em dicionários

pessoa = {}
chave = 'nome'
pessoa[chave] = 'João'
pessoa['sobrenome'] = 'Sales'
print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Maria'
print(pessoa)

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

print()
# print(pessoa.get('sobrenome', 'Chave não existe'))
# print(pessoa.get('sobrenome', None))
# pessoa['sobrenome'] = 'Sales'
if pessoa.get('sobrenome') is None:
    print('Chave não existe')
else:
    print(pessoa['sobrenome'])
