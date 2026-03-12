"""
Introdução a Packages (Pacotes) em Python

Packages são estruturas usadas para organizar módulos em diretórios.
Eles permitem dividir um projeto em partes menores, facilitando a
manutenção, reutilização e organização do código.

Módulo:
    Um arquivo Python (.py)

Package:
    Uma pasta que contém módulos ou outros packages.

Estrutura básica de um package:

    projeto/
        main.py
        usuarios/
            __init__.py
            cadastro.py

O arquivo __init__.py tradicionalmente marca o diretório como um package
e pode executar código quando o package é importado. Ele também pode ser
usado para expor funcionalidades específicas do package.

Exemplo de módulo dentro do package:

    cadastro.py

        def criar_usuario(nome):
            print(f'Usuário {nome} criado')

Importando o módulo:

    from usuarios.cadastro import criar_usuario
    criar_usuario("João")

Também é possível organizar packages dentro de packages
(subpackages):

    sistema/
        __init__.py
        usuarios/
            __init__.py
            cadastro.py

Import:

    from sistema.usuarios.cadastro import criar_usuario


IMPORTS RELATIVOS

Dentro de packages é possível usar imports relativos para acessar
outros módulos do mesmo package.

Exemplo:

    from .cadastro import criar_usuario
    from ..banco import conectar

Significado:

    .   → mesmo package
    ..  → um nível acima


USO DE __all__

O atributo especial __all__ é usado para definir explicitamente
quais nomes um módulo ou package exporta quando se utiliza:

    from modulo import *

Exemplo no arquivo __init__.py:

    from .cadastro import criar_usuario
    from .autenticacao import login

    __all__ = ["criar_usuario", "login"]

Agora, ao usar:

    from usuarios import *

Somente os nomes definidos em __all__ serão importados.

Sem __all__, o comportamento do import * pode expor mais nomes
do que o desejado, incluindo variáveis internas do módulo.


PYTHON MODERNO E __init__.py

Desde o Python 3.3 existem os chamados Namespace Packages,
que permitem criar packages mesmo sem o arquivo __init__.py.

Porém, na prática profissional ainda é comum manter o
arquivo __init__.py para:

    - evitar ambiguidades
    - manter compatibilidade
    - controlar exportações com __all__
    - inicializar o package


RESUMO

Arquivo .py           → módulo
Pasta com módulos     → package
Package dentro de outro → subpackage

Packages são essenciais para organizar projetos Python maiores
e permitem estruturar o código de forma modular e escalável.
"""

# https://stackoverflow.com/questions/2386714/why-is-import-bad

# from sys import path

# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import soma_do_modulo, fala_oi
# from aula99_package.modulo import *

# print(__name__)
# print(*path, sep='\n')


# print(aula99_package.modulo.soma_do_modulo(2, 3))
# print(modulo.soma_do_modulo(2, 3))
# print(soma_do_modulo(2, 3))
# print(variavel)
# print(nova_variavel)

# aula99_package.modulo.fala_oi()
# modulo.fala_oi()
# fala_oi()

# import aula99_package
from aula99_package import soma_do_modulo, falar_oi

# print(aula99_package.dobra(2))
# print(aula99_package.soma_do_modulo(2, 3))
print(soma_do_modulo(2, 3))
# print(aula99_package.variavel)
# print(aula99_package.nova_variavel)
falar_oi()