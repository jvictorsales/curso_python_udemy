# Introdução a generator functions em Python
# generator = (n for n in range(1000000))

# def generator():
#     yield 1  # Pausar
#     print('Continuando...')
#     yield 2  # Pausar
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'

# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for n in gen:
#     print(n)


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

# gen = generator(n=5, maximum=8)
gen = generator(maximum=1000000)
for n in gen:
    print(n)
