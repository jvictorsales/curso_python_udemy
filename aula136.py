# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO,', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)

cliente_1 = Cliente('Maria')
cliente_1.inserir_endereco('Av Brasil', 54)
cliente_1.inserir_endereco('Rua B', 45)
# print(cliente_1.enderecos[0].rua)
# print(cliente_1.enderecos[1].rua)
endereco_externo = Endereco('Av Saudade', 123321)
cliente_1.inserir_endereco_externo(endereco_externo)
cliente_1.listar_enderecos()
print()

del cliente_1

print()
print(endereco_externo.rua, endereco_externo.numero)
print()

print('##### AQUI TERMINA MEU CÓDIGO #####')
print()
