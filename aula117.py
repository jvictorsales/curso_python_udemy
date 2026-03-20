import json
import os

# pessoas = [
#     {
#         'nome': 'João',
#         'sobrenome': 'Sales',
#         'idade': 22,
#         'ativo': True,
#         'notas': ['A', 'A+'],
#         'telefones': {
#             'residencial': '00 0000-0000',
#             'celular': '00 0000-0000',
#         },
#         'enderecos': [
#             {'rua': 'R1', 'numero': 32},
#             {'rua': 'R2', 'numero': 55},
#         ],
#         'altura': 1.8,
#         'numeros_preferidos': (2, 4, 6, 8, 10),
#         'dev': True,
#         'nada': None,
#     },
#     {
#         'nome': 'Maria',
#         'sobrenome': 'Vieira',
#         'idade': 18,
#         'ativo': False,
#         'notas': ['B', 'A'],
#         'telefones': {
#             'residencial': '00 0000-0000',
#             'celular': '00 0000-0000',
#         },
#         'enderecos': [
#             {'rua': 'R25', 'numero': 18},
#             {'rua': 'R35', 'numero': 29},
#         ],
#         'altura': 1.55,
#         'numeros_preferidos': (10, 18, 21, 45, 54),
#         'dev': False,
#         'nada': None,
#     },
# ]

# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(SAVE_TO, 'w') as file:
#     json.dump(pessoas, file, indent=2)

# print(json.dumps(pessoas, indent=2))

# BASE_DIR = os.path.dirname(__file__)
# JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(JSON_FILE, 'r') as file:
#     pessoas = json.load(file)
#     print(json.dumps(pessoas))
    # for pessoa in pessoas:
    #     print(pessoa['nome'])


# json_string = '''
# [{"nome": "Joao", "sobrenome": "Sales", "idade": 22, "ativo": true, "notas": ["A", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}, "enderecos": [{"rua": "R1", "numero": 32}, {"rua": "R2", "numero": 55}], "altura": 1.8, "numeros_preferidos": [2, 4, 6, 8, 10], "dev": true, "nada": null}, {"nome": "Maria", "sobrenome": "Vieira", "idade": 18, "ativo": false, "notas": ["B", "A"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}, "enderecos": [{"rua": "R25", "numero": 18}, {"rua": "R35", "numero": 29}], "altura": 1.55, "numeros_preferidos": [10, 18, 21, 45, 54], "dev": false, "nada": null}]
# '''

# pessoas = json.loads(json_string)
# print(pessoas)

# for pessoa in pessoas:
#     # print(pessoa['nome'])
#     print(pessoa)


pessoa = {
    'nome': 'João 2',
    'sobrenome': 'Sales',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2, ensure_ascii=False)

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
