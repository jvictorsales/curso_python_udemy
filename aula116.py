"""
Manipulação de Arquivos em Python

A função `open()` é utilizada para abrir arquivos em Python. O arquivo pode ou não existir,
dependendo do modo utilizado.

Modos de abertura:
    r  -> leitura (erro se o arquivo não existir)
    w  -> escrita (cria ou sobrescreve o arquivo)
    x  -> criação exclusiva (erro se o arquivo já existir)
    a  -> append (adiciona conteúdo ao final do arquivo)
    b  -> modo binário
    t  -> modo texto (padrão)
    +  -> leitura e escrita combinadas (ex: r+, w+)

Uso recomendado:
    Utilizar o "context manager" com `with`, pois ele garante que o arquivo será
    fechado automaticamente após o uso.

    Exemplo:
        with open('arquivo.txt', 'w') as arquivo:
            arquivo.write('Olá mundo')

Métodos úteis:
    write(texto)        -> escreve uma string no arquivo
    writelines(lista)   -> escreve múltiplas linhas (não adiciona quebra de linha automaticamente)
    read()              -> lê todo o conteúdo do arquivo
    readline()          -> lê uma única linha
    readlines()         -> retorna uma lista com todas as linhas
    seek(posicao)       -> move o cursor para uma posição específica no arquivo

Cursor:
    O arquivo possui um cursor interno que indica a posição atual de leitura/escrita.
    O método `seek()` permite reposicionar esse cursor.

Módulo os:
    Permite manipular arquivos no sistema operacional.

    os.remove(caminho)  -> remove um arquivo
    os.unlink(caminho)  -> remove um arquivo (equivalente ao remove)
    os.rename(origem, destino) -> renomeia ou move um arquivo

Módulo json:
    Utilizado para trabalhar com dados no formato JSON.

    json.dump(dado, arquivo) -> escreve dados em formato JSON no arquivo
    json.load(arquivo)       -> lê dados JSON de um arquivo e converte para estruturas Python

Observações:
    - Sempre prefira usar `with open(...)` para evitar vazamento de recursos.
    - O modo 'w' apaga o conteúdo anterior do arquivo.
    - O modo 'a' preserva o conteúdo existente e adiciona ao final.
"""

import os

# caminho_arquivo = r'C:\\Estudos\\exercicios_python\\'
# caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

caminho_arquivo = 'aula116.txt'

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print('Lendo - read()')
#     print(arquivo.read())

#     arquivo.write('Linha 5\n')
    
#     print('Lendo - readline()')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('Lendo - readlines()')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print()
# print('#' * 10)
# print()

# with open(caminho_arquivo, 'r') as arquivo:
#     print('Lendo - read()')
#     print(arquivo.read())


with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')
