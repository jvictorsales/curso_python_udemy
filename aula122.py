"""
Módulo: Métodos de Instância em Classes Python

Descrição:
    Métodos de instância são funções definidas dentro de uma classe que operam
    sobre os dados da instância (objeto). Eles permitem encapsular comportamentos
    relacionados aos atributos do objeto, promovendo organização e reutilização
    de código.

Conceitos principais:

    - Método de instância:
        Função definida dentro de uma classe que recebe como primeiro parâmetro
        uma referência à instância (convencionalmente chamada de 'self').

    - self:
        Representa a instância atual do objeto. É utilizado para acessar e
        modificar atributos e chamar outros métodos da mesma classe.

    - __init__:
        Método construtor chamado automaticamente ao criar uma instância.
        Usado para inicializar atributos do objeto.

    - Encapsulamento:
        Métodos ajudam a manter dados e comportamentos relacionados dentro
        da mesma estrutura (classe).

Exemplo:

    class Pessoa:
        def __init__(self, nome):
            self.nome = nome

        def falar(self):
            print(f"{self.nome} está falando")

    p1 = Pessoa("João")
    p1.falar()

Hard coded:

    - Definição:
        Hard coded refere-se à prática de inserir valores fixos diretamente
        no código, tornando-o menos flexível e reutilizável.

    - Exemplo ruim:

        def falar(self):
            print("João está falando")

    - Exemplo correto:

        def falar(self):
            print(f"{self.nome} está falando")

    - Problemas:
        * Baixa reutilização
        * Dificuldade de manutenção
        * Código inflexível

Boas práticas:

    - Sempre utilizar 'self' para acessar atributos
    - Evitar valores hard coded dentro de métodos
    - Criar métodos com responsabilidade única
    - Utilizar nomes claros e descritivos
    - Preferir dados dinâmicos (parâmetros ou atributos)

Conclusão:

    Métodos de instância são fundamentais na programação orientada a objetos
    em Python, pois permitem que objetos tenham comportamentos próprios e
    manipulem seus dados de forma organizada. Evitar hard coding contribui
    para um código mais flexível, reutilizável e fácil de manter.
"""

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

print()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
