"""
Entendendo módulos e importações em Python.

Em Python, todo arquivo .py é considerado um módulo. O primeiro
arquivo executado pelo interpretador é chamado de módulo principal
do programa e recebe o nome especial "__main__".

Quando um arquivo é executado diretamente, a variável especial
__name__ recebe o valor "__main__". Isso permite diferenciar se
um arquivo está sendo executado diretamente ou apenas importado
como módulo em outro script.

Exemplo:

    print(__name__)

Se o arquivo for executado diretamente:
    __main__

Se for importado:
    nome_do_modulo


Importação de módulos
---------------------

Python permite importar módulos de diferentes formas:

1) Importar o módulo inteiro:

    import math
    print(math.sqrt(9))

Nesse caso utilizamos o namespace do módulo.

2) Importar partes específicas do módulo:

    from math import sqrt
    print(sqrt(9))

Aqui a função pode ser usada diretamente.

3) Importar com alias (apelido):

    import math as m
    print(m.sqrt(9))


Como o Python encontra módulos
------------------------------

Quando utilizamos a instrução "import", o Python procura o módulo
em vários diretórios. Esses diretórios estão listados na variável
sys.path.

Exemplo:

    import sys
    print(sys.path)

O sys.path é uma lista contendo os caminhos onde o Python procura
módulos e pacotes.


Locais onde o Python procura módulos
------------------------------------

1) Diretório do script principal (__main__)
2) Pastas dentro do projeto
3) Bibliotecas padrão do Python
4) Diretórios site-packages (bibliotecas instaladas via pip)


Estrutura de projeto
--------------------

Python consegue importar facilmente módulos que estão na mesma
pasta ou em subpastas do projeto.

Exemplo:

    projeto/
    ├── main.py
    └── utils/
        └── calculo.py

Dentro de main.py é possível fazer:

    from utils import calculo


Pastas acima do módulo principal
--------------------------------

Por padrão, Python não procura módulos em pastas acima do arquivo
principal executado (__main__). Para importar módulos fora dessa
estrutura é necessário:

- Ajustar o PYTHONPATH
- Modificar manualmente o sys.path
- Instalar o pacote
- Estruturar o projeto como pacote Python


Resumo
------

- Todo arquivo .py é um módulo
- O primeiro arquivo executado chama-se "__main__"
- Python procura módulos nos caminhos definidos em sys.path
- Subpastas do projeto são reconhecidas automaticamente
- Pastas acima do módulo principal não são reconhecidas por padrão
"""


# try:
#     import sys
#     sys.path.append(r'C:\Users\root\Desktop')
# except ModuleNotFoundError:
#     print('Módulo não encontrado.')

import sys
import aula97_m
# import qualquer

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')
