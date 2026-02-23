# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador_de_numeros(multiplicador):
    def multiplicar_numero(numero):
        return (numero * multiplicador)
    return multiplicar_numero

duplicar = multiplicador_de_numeros(2)
triplicar = multiplicador_de_numeros(3)
quadruplicar = multiplicador_de_numeros(4)

print(duplicar(2))
print(duplicar(10))
print(duplicar(16))

print()

print(triplicar(10))
print(triplicar(20))
print(triplicar(30))

print()

print(quadruplicar(2))
print(quadruplicar(4))
print(quadruplicar(8))
