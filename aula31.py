"""
Flags (bandeiras) em Python são usadas para marcar um estado ou condição
dentro do código. Normalmente, uma flag é representada por um valor que
indica se algo já aconteceu, se uma condição foi atendida ou se um fluxo
de execução deve seguir por um determinado caminho.

O valor None representa a ausência de valor. Ele é diferente de zero,
string vazia ou False. None indica que uma variável existe, mas ainda não
possui um valor significativo atribuído a ela.

Os operadores 'is' e 'is not' são usados para verificar identidade, ou seja,
eles testam se duas variáveis apontam para o mesmo objeto na memória, e não
apenas se possuem valores iguais.

Por isso, 'is' e 'is not' são a forma correta de comparar com None, já que
None é um objeto único em Python.

A função id() retorna a identidade de um objeto, que corresponde ao seu
endereço na memória durante a execução do programa. Se dois objetos possuem
o mesmo id, significa que ambos fazem referência ao mesmo objeto.

Em resumo:
- Flags ajudam a controlar o fluxo do programa
- None indica ausência de valor
- 'is' e 'is not' verificam identidade, não igualdade
- id() mostra a identidade (referência na memória) de um objeto
"""


condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)


# if passou_no_if is None:
#     print('Não passou no if')

# if passou_no_if is not None:
#     print('Passou no if')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')


print('-' * 10)

variavel_1 = 'a'
variavel_2 = 'a'

print(id(variavel_1))
print(id(variavel_2))
