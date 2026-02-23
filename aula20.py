primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

if primeiro_valor_int > segundo_valor_int:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
elif primeiro_valor_int < segundo_valor_int:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')
else:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
