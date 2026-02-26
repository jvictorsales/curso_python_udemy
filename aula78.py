"""
Sets (Conjuntos) em Python

Em Python, o tipo `set` representa um conjunto matemático: 
uma coleção de elementos **únicos**, **não ordenados** e **sem índices**.

Assim como na matemática, conjuntos são usados para agrupar valores
sem repetição e permitem operações clássicas como união, interseção
e diferença (normalmente ilustradas por diagramas de Venn).
"""

s1 = set('João')
print(s1, type(s1))

s1 = {'João', 1, 2, 3}
print(s1, type(s1))

"""
Características principais dos sets:
- São mutáveis (podem ser alterados após a criação);
- Aceitam apenas valores imutáveis como elementos internos
  (int, float, str, tuple, etc.);
- Não permitem valores duplicados;
- Não possuem índices nem garantem ordem dos elementos;
- São iteráveis (podem ser usados com for);
- Suportam os operadores `in` e `not in` para verificação de pertencimento.

Uso comum:
- Remover valores duplicados de iteráveis;
- Testar pertencimento de forma eficiente;
- Realizar operações matemáticas entre conjuntos de dados.
"""

s1 = {1, 2, 3, 3, 3, 3, 3, 3, 1}
l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
print('lista l1:', l1)

s1 = set(l1)
print('set s1:', s1)

l2 = list(s1)
print('lista l2:', l2)

print()
s1 = {1, 2, 3}
print(3 in s1)
print(3 not in s1)

for numero in s1:
    print(numero)

"""
Principais métodos dos sets:
- add(elem): adiciona um único elemento ao conjunto;
- update(iterável): adiciona vários elementos de um iterável;
- discard(elem): remove um elemento sem gerar erro se ele não existir;
- clear(): remove todos os elementos do conjunto.
"""

s1 = set()
s1.add('João')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('João')
print(s1)

"""
Operações entre sets:
- União (| ou union): combina os elementos de dois conjuntos;
- Interseção (& ou intersection): elementos comuns aos dois conjuntos;
- Diferença (-): elementos que existem apenas no conjunto da esquerda;
- Diferença simétrica (^): elementos que não estão presentes em ambos
  os conjuntos ao mesmo tempo.
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s1 ^ s2
s8 = s2 ^ s1
print('set s1:', s1)
print('set s2:', s2)
print('união:', s3)
print('intersecção:', s4)
print('diferença s1 - s2:', s5)
print('diferença s2 - s1:', s6)
print('diferença simétrica:', s7)
print('diferença simétrica:', s8)
