# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2026  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')    
        
    @classmethod
    def cria_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)
    
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

p1 = Pessoa('Ana', 50)
p2 = Pessoa.cria_com_50_anos('Ana')

p3 = Pessoa('Anônima', 25)
p4 = Pessoa.criar_sem_nome(25)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)