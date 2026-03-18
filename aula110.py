# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Luíz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'D'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Ruth', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
# grupos = groupby(sorted(alunos))
# print(*list(grupos), sep='\n')


def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

# for aluno in alunos_agrupados:
#     print(aluno)

grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    # print(*list(grupo), sep='\n')
    for aluno in grupo:
        print(aluno)
