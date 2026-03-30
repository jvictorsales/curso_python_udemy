# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crei uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome


fiat = Fabricante('Fiat')
motor_1_0 = Motor('1.0')
fiat_uno = Carro('Uno')
fiat_uno.motor = motor_1_0
fiat_uno.fabricante = fiat

chevrolet = Fabricante('Chevrolet')
motor_2_0 = Motor('2.0')
opala = Carro('Opala')
opala.motor = motor_2_0
opala.fabricante = chevrolet

ford = Fabricante('Ford')
focus = Carro('Focus Titanium')
focus.motor = motor_2_0
focus.fabricante = ford

print(opala.nome, opala.motor.nome, opala.fabricante.nome)
print(fiat_uno.nome, fiat_uno.motor.nome, fiat_uno.fabricante.nome)
print(focus.nome, focus.motor.nome, focus.fabricante.nome)
