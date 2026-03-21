"""
Explica o problema de parâmetros mutáveis como valores padrão em funções Python.

Em Python, os valores padrão dos parâmetros são avaliados apenas uma vez,
no momento em que a função é definida, e não a cada chamada da função.
Isso significa que, se um valor padrão for um objeto mutável (como lista,
dicionário ou conjunto), esse mesmo objeto será reutilizado em todas as
execuções da função.

Esse comportamento pode causar efeitos colaterais inesperados, pois alterações
feitas no objeto persistem entre chamadas.

Exemplo problemático:
    def adicionar_item(item, lista=[]):
        lista.append(item)
        return lista

    adicionar_item(1)  # [1]
    adicionar_item(2)  # [1, 2]  # comportamento inesperado

Nesse caso, a lista padrão é compartilhada entre todas as chamadas.

Forma correta:
    def adicionar_item(item, lista=None):
        if lista is None:
            lista = []
        lista.append(item)
        return lista

Aqui, uma nova lista é criada a cada chamada quando nenhum valor é fornecido.

Boas práticas:
    - Evitar usar objetos mutáveis como valores padrão de parâmetros.
    - Utilizar None como valor padrão e inicializar o objeto dentro da função.

Observação:
    Esse comportamento pode ser usado intencionalmente para manter estado
    entre chamadas, mas essa prática não é recomendada em código de produção,
    pois reduz a legibilidade e pode causar bugs difíceis de rastrear.
"""

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

# lista_1 = []
cliente_1 = adiciona_clientes('João')
adiciona_clientes('Luiz', cliente_1)
adiciona_clientes('Fernando', cliente_1)
cliente_1.append('Edu')

cliente_2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente_2)

cliente_3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente_3)

print(cliente_1)
print(cliente_2)
print(cliente_3)
