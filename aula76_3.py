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

pessoa = {
    'nome': 'João',
    'sobrenome': 'Sales',
    # 'idade': 25,
}

# print(pessoa.__len__())
# print(len(pessoa))

# print(list(pessoa.keys()))
# print(tuple(pessoa.keys()))

# for chave in pessoa.keys():
#     print(chave)

# for chave in pessoa:
#     print(chave)

# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault('idade', None)
print(pessoa['idade'])
