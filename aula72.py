# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar_numeros(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado_da_multiplicacao = multiplicar_numeros(2, 3, 4, 5)
print(f'Total = {resultado_da_multiplicacao}')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# def par_ou_impar(*args):
#     for numero in args:
#         numero_par = numero % 2 == 0 
#         if numero_par:
#             print(f'O número {numero} é par.')
#         else:
#             print(f'O número {numero} é ímpar.')
                
# par_ou_impar(1, 2, 3, 4, 5)

def par_ou_impar(numero):
    numero_par = numero % 2 == 0

    if numero_par:
        return f'O número {numero} é par.'
    
    return f'O número {numero} é ímpar.'

print(par_ou_impar(15))
print(par_ou_impar(10))
