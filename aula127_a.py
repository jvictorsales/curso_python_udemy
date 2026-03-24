# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula127.json'

def salvar_dados_classe(caminho_arquivo, lista_objetos):
    print('Fazendo Dump')
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista_objetos, arquivo, indent=2, ensure_ascii=False)


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

if __name__ == '__main__':

    p1 = Pessoa('João', 'Sales', 35)
    p2 = Pessoa('Ruth', 'Batista', 30)
    p3 = Pessoa('Helena', 'Santos', 18)

    # dados_pessoas = [vars(p1), p2.__dict__, vars(p3)]
    dados_pessoas = []
    dados_pessoas.append(vars(p1))
    dados_pessoas.append(vars(p2))
    dados_pessoas.append(vars(p3))

    salvar_dados_classe(CAMINHO_ARQUIVO, dados_pessoas)
