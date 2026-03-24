import json

from aula127_a import CAMINHO_ARQUIVO, Pessoa

def ler_dados_classe(caminho_arquivo):
    dados_classe = None
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        dados_classe = json.load(arquivo)
    
    return dados_classe

if __name__ == '__main__':
    
    lista_pessoas = ler_dados_classe(CAMINHO_ARQUIVO)

    dados_p1, dados_p2, dados_p3, *_ = lista_pessoas

    # p1 = Pessoa(**lista_pessoas[0])
    # p2 = Pessoa(**lista_pessoas[1])
    # p3 = Pessoa(**lista_pessoas[2])

    p1 = Pessoa(**dados_p1)
    p2 = Pessoa(**dados_p2)
    p3 = Pessoa(**dados_p3)

    # print(vars(p1))
    # print(vars(p2))
    # print(vars(p3))
    print(p1.nome, p1.sobrenome, p1.idade)
    print(p2.nome, p2.sobrenome, p2.idade)
    print(p3.nome, p3.sobrenome, p3.idade)
