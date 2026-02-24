"""
Métodos úteis dos dicionários em Python

Os dicionários possuem diversos métodos embutidos que facilitam
a manipulação, consulta e atualização dos dados armazenados
em pares de chave e valor.

len(dicionario):
- Retorna a quantidade de chaves no dicionário.
- Não conta valores, apenas chaves.

keys():
- Retorna um iterável (dict_keys) contendo todas as chaves.
- Pode ser usado em loops (for) ou convertido em lista.

values():
- Retorna um iterável (dict_values) contendo todos os valores.
- A ordem segue a ordem de inserção das chaves.

items():
- Retorna um iterável (dict_items) com pares (chave, valor).
- Muito usado para percorrer chaves e valores ao mesmo tempo.

setdefault(chave, valor_padrao):
- Retorna o valor da chave se ela existir.
- Se a chave NÃO existir, ela é criada com o valor padrão informado.
- Útil para evitar verificações manuais de existência da chave.

copy():
- Retorna uma cópia rasa (shallow copy) do dicionário.
- A estrutura externa é copiada, mas objetos mutáveis internos
  continuam sendo compartilhados.

get(chave, valor_padrao=None):
- Retorna o valor da chave se ela existir.
- Se a chave não existir, retorna o valor padrão (None por padrão).
- Evita o erro KeyError ao acessar chaves inexistentes.

pop(chave[, valor_padrao]):
- Remove a chave especificada e retorna o valor correspondente.
- Se a chave não existir:
  - Lança KeyError (sem valor padrão)
  - Retorna o valor padrão, se informado

popitem():
- Remove e retorna o último par (chave, valor) inserido.
- Muito útil para desempilhar dados.
- Em dicionários vazios, gera KeyError.

update(outro_dicionario ou iterável):
- Atualiza o dicionário com novos pares chave-valor.
- Se a chave já existir, o valor será sobrescrito.
- Pode receber:
  - Outro dicionário
  - Iterável de pares (chave, valor)
  - Argumentos nomeados

Observação importante:
- Todos esses métodos operam diretamente no dicionário original,
  exceto copy(), que cria uma nova referência.
"""

p1 = {
    'nome': 'João',
    'sobrenome': 'Sales',
}

print(p1['nome'])
print(p1.get('nome'))
print(p1.get('nome1'))
print(p1.get('nome1', 'Não existe'))

print()

# del p1['nome']
# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Victor',
#     'idade': 30
# })

# p1.update(nome='Victor', idade=30)

# tupla = ('nome', 'Victor'), ('idade', 30)
# p1.update((('nome', 'Victor'), ('idade', 30)))
# p1.update(tupla)

lista = [['nome', 'Victor'], ['idade', 30]]
p1.update(lista)
# p1.update([['nome', 'Victor'], ['idade', 30]])
print(p1)


# print()
# dicionario_de_frutas = {}
# lista_de_frutas = ['Banana', 'Maçã', 'Kiwi']
# iteravel = enumerate(lista_de_frutas)
# dicionario_de_frutas.update(iteravel)
# print(dicionario_de_frutas)
