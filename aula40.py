"""
Calculadora com while
"""

while True:

    primeiro_numero = input('Digite o primeiro número: ').strip()
    segundo_numero = input('Digite o segundo número: ').strip()
    operador = input('Digite o operador [ + - * / ]: ').strip()
    
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
    except ValueError:
        print('O valor informado não é um número, tente novamente.')
        continue
    
    if operador == '+':
        resultado = primeiro_numero_float + segundo_numero_float
    elif operador == '-':
        resultado = primeiro_numero_float - segundo_numero_float
    elif operador == '*':
        resultado = primeiro_numero_float * segundo_numero_float
    elif operador == '/':
        if segundo_numero_float == 0:
            print('Não é possível dividir por zero.')
            continue
        resultado = primeiro_numero_float / segundo_numero_float
    else:
        print('Operador inválido, tente novamente.')
        continue

    print(f'O resultado da operação {primeiro_numero_float} {operador} {segundo_numero_float} = {resultado:.2f}')        
    
    sair = input('Deseja sair? [s/n] ').strip().lower().startswith('s')

    if sair:
        print('Saindo...')
        break
