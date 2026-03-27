"""
Encapsulamento em Python

Diferente de outras linguagens, Python não possui modificadores de acesso
reais (public, protected, private). Em vez disso, utiliza convenções de nomenclatura
para indicar a intenção de uso dos atributos e métodos.

Tipos de acesso por convenção:

1. Public (sem underline)
   - Ex: self.nome
   - Pode ser acessado de qualquer lugar.
   - Representa a interface pública da classe.

2. Protected (_um underline)
   - Ex: self._nome
   - Indica que o atributo é interno e não deve ser acessado fora da classe
     ou de suas subclasses.
   - Não há proteção real, apenas convenção.

3. Private (__dois underlines)
   - Ex: self.__nome
   - Ativa o mecanismo de "name mangling", onde o Python renomeia o atributo
     internamente para evitar conflitos.
   - Ex: _NomeClasse__nome
   - Evita sobrescrita acidental em herança, mas não impede acesso externo.

Name Mangling:
   - Serve para evitar colisões de nomes em subclasses.
   - Não é uma forma de segurança, apenas uma proteção contra uso acidental.

Encapsulamento real em Python:
   - É feito principalmente com uso de @property e setters.
   - Permite controlar leitura e escrita de atributos.

Filosofia do Python:
   - "Somos todos adultos responsáveis" (consenting adults)
   - O acesso não é impedido, mas sim desencorajado quando necessário.

Boas práticas:
   - Use atributos públicos para interface da classe.
   - Use _ (protected) para atributos internos.
   - Use __ (private) apenas quando necessário (ex: evitar conflitos em herança).
"""

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        # print(self.__private)
        # self.__metodo_privado()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        # print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_privado(self):
        # print('_metodo_privado')
        return '__metodo_privado'

f = Foo()
print(f.public)
# print(f._protected)  # funciona mas não deveria estar aqui
print(f.metodo_publico())
# print(f._metodo_protected())  # funciona mas não deveria estar aqui
# print(f._Foo__metodo_privado())
