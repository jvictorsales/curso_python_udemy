"""
Iteráveis e Iteradores em Python

Um iterável é qualquer objeto que pode ser percorrido elemento por elemento.
Exemplos comuns de iteráveis são: str, list, tuple, dict, set e range.
Esses objetos não entregam valores diretamente, mas sabem como gerar
um iterador a partir deles.

Um iterador é o objeto responsável por entregar os valores, um de cada vez.
Ele mantém o controle de qual é o "próximo" elemento da sequência e lembra
seu estado interno durante a iteração.

A função iter() é usada para obter o iterador de um objeto iterável.
Ou seja, ela pede ao iterável que forneça seu iterador.

A função next() é usada para solicitar ao iterador o próximo valor disponível.
Cada chamada a next() avança o iterador.
Quando não há mais valores a serem entregues, o iterador lança a exceção
StopIteration.

Em resumo:
- Iterável: objeto que pode ser percorrido (ex.: str, range).
- Iterador: objeto que sabe entregar um valor por vez.
- iter(): obtém o iterador a partir de um iterável.
- next(): obtém o próximo valor do iterador.
"""


# texto = 'Victor'.__iter__()
# texto = iter('Victor')
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())  # StopIteration
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))  # StopIteration

texto_2 = 'João'  # iterável
iterador = iter(texto_2)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

print()

for letra in texto_2:
    print(letra)
