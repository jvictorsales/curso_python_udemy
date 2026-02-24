"""
Dicionários em Python (dict)

Dicionários são estruturas de dados que armazenam informações
no formato de pares "chave: valor".

Diferente de listas e tuplas, que acessam dados por posição
(índice numérico), os dicionários utilizam chaves para acessar
seus valores. Essas chaves funcionam como identificadores
únicos dentro do dicionário.

Características principais:
- Cada chave aponta para um valor.
- As chaves devem ser únicas (não podem se repetir).
- Os valores podem se repetir livremente.
- A ordem de inserção é preservada (Python 3.7+).

Tipos permitidos para as chaves:
As chaves precisam ser de tipos imutáveis, como:
- str
- int
- float
- bool
- tuple

Isso é necessário porque o Python precisa garantir que a chave
não mude ao longo do tempo, permitindo acesso rápido e seguro.

Tipos permitidos para os valores:
- Qualquer tipo de dado é aceito:
  int, float, str, bool, list, tuple, dict, objetos, etc.
- Um dicionário pode conter outro dicionário (estruturas aninhadas).

Criação de dicionários:
- Usando chaves {}:
    pessoa = {'nome': 'João', 'idade': 30}

- Usando a classe dict:
    pessoa = dict(nome='João', idade=30)

Mutabilidade:
- dict é um tipo mutável:
  Podemos adicionar, alterar ou remover pares chave-valor.
- Tipos mutáveis comuns:
  dict, list
- Tipos imutáveis comuns:
  str, int, float, bool, tuple

Uso comum:
Dicionários são ideais para representar dados estruturados,
como registros, configurações, JSONs, objetos do mundo real
e qualquer situação em que seja necessário associar um valor
a um identificador.
"""

# pessoa = dict(nome='João', sobrenome='Sales', idade=25)
pessoa = {
    'nome': 'João',
    'sobrenome': 'Sales',
    'idade': 25,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
