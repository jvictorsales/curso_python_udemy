# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class

# class Foo(object):
# class Foo:
#     ...
# help(Foo)

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('EITA, nem saí da classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'

cliente_1 = Cliente('João', 'Sales')
cliente_1.falar_nome_classe()

aluno_1 = Aluno('Maria', 'Helena')
aluno_1.falar_nome_classe()

print(aluno_1.cpf)

# help(Cliente)
