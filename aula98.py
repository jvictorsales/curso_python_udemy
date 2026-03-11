"""
Recarregando módulos, importlib e Singleton em Python

Quando um módulo é importado em Python, ele é executado apenas uma vez
e armazenado em cache dentro de sys.modules. Importações subsequentes
não executam o módulo novamente, apenas reutilizam o objeto já carregado.

Isso faz com que módulos funcionem naturalmente como Singletons,
pois todos os imports retornam a mesma instância do módulo.

Em situações onde é necessário reexecutar o código de um módulo,
como durante desenvolvimento interativo ou sistemas de plugins,
podemos utilizar importlib.reload().

Exemplo:

    import importlib
    import modulo

    importlib.reload(modulo)

O reload reexecuta o código do módulo, atualizando seus atributos.
Entretanto, objetos importados diretamente com "from modulo import nome"
não são atualizados automaticamente, pois passam a referenciar o valor
antigo.

Por isso, quando existe a necessidade de recarregar módulos, recomenda-se
importar o módulo completo e acessar seus atributos através do namespace.

Resumo:
- Módulos são carregados uma única vez
- Python utiliza sys.modules como cache
- importlib.reload() permite reexecutar o módulo
- Módulos funcionam naturalmente como Singletons
"""

import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')
