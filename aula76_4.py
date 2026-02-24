"""
Shallow Copy e Deep Copy em Python com dicionários

Ao trabalhar com dicionários em Python, é importante compreender a diferença
entre Shallow Copy (cópia rasa) e Deep Copy (cópia profunda), pois isso afeta
como os dados são compartilhados na memória.

----------------------------------------------------------------------
Shallow Copy (Cópia Rasa)
----------------------------------------------------------------------

A shallow copy cria um novo dicionário, mas não cria novos objetos para os
valores internos. As referências aos objetos armazenados como valores são
mantidas.

Isso significa que:
- O dicionário externo é um novo objeto
- Os valores internos mutáveis continuam compartilhados
- Alterações em objetos mutáveis internos refletem em todas as cópias

Métodos comuns para criar uma shallow copy incluem:
- dict.copy()
- dict(original)
- copy.copy()

----------------------------------------------------------------------
Deep Copy (Cópia Profunda)
----------------------------------------------------------------------

A deep copy cria um novo dicionário e copia recursivamente todos os objetos
internos, criando estruturas completamente independentes.

Características principais:
- Nenhuma referência interna é compartilhada
- Alterações em qualquer nível não afetam o dicionário original
- Requer o uso do módulo copy

Método utilizado:
- copy.deepcopy()
"""

import copy

d1 = {
  'c1': 1,
  'c2': 2,
  'l1': [0, 1, 2],
}

# d2 = d1
# d2 = d1.copy()
# d2 = copy.copy(d1)
d2 = copy.deepcopy(d1)

print(f'd1: {d1}', id(d1))
print(f'd2: {d2}', id(d2))

print()

d2['c1'] = 1000
d2['l1'][0] = 9999

print(f'd1: {d1}', id(d1))
print(f'd2: {d2}', id(d2))
