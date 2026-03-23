# Atributos de classe

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 100

    def get_ano_nascimento(self):
        # return self.ano_atual - self.idade
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 18)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
