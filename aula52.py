"""
Tipo tupla - Uma lista imutável
"""

nomes = 'Maria', 'Helena', 'João'
print(nomes[0])
print(nomes[-1])
print(nomes, type(nomes))

nomes = ('Maria', 'Helena', 'João')
print(nomes, type(nomes))

nomes = ['Maria', 'Helena', 'João']
nomes = tuple(nomes)
print(nomes, type(nomes))
