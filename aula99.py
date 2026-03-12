"""
Introdução a Packages (Pacotes) em Python

Packages são estruturas usadas para organizar módulos em diretórios.
Eles permitem dividir um projeto em partes menores e mais organizadas.

Módulo:
    Um arquivo Python (.py)

Package:
    Uma pasta que contém módulos ou outros packages

Estrutura básica:

    projeto/
        main.py
        usuarios/
            __init__.py
            cadastro.py

O arquivo __init__.py marca o diretório como um package e pode
executar código ou expor funcionalidades quando o package é importado.

Exemplo de import:

    from usuarios.cadastro import criar_usuario

Também é possível organizar packages dentro de packages
(subpackages), criando hierarquias maiores:

    sistema/
        usuarios/
            cadastro.py

Import:

    from sistema.usuarios.cadastro import criar_usuario

Packages são fundamentais para organizar projetos Python
maiores, evitando conflitos de nomes e facilitando manutenção.
"""

from sys import path

import aula99_package.modulo
from aula99_package import modulo
# from aula99_package.modulo import soma_do_modulo
from aula99_package.modulo import *

print(__name__)
print(*path, sep='\n')


print(aula99_package.modulo.soma_do_modulo(2, 3))
print(modulo.soma_do_modulo(2, 3))
print(soma_do_modulo(2, 3))
print(variavel)
print(nova_variavel)
