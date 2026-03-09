# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindedx.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys
# sys.exit()
# "sys." É o namespace do módulo
# platform = 'A minha'
# print(sys.platform)
# print(plataform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform
# print(platform)
# print('Oi')
# exit()

# alias 1 - import nome_modulo as apelido

# import sys as s
# sys = 'Alguma coisa'
# print(sys)
# print(s.platform)

# alias 2 - from nome_modulo import objeto as apelido

# from sys import exit as ex, platform as pf
# from sys import exit as ex
# from sys import platform as pf
# print(pf)
# ex()

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

# from sys import *
# print(platform)
# exit()