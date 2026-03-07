# Try, except, else e finally

string = 'João'  # str
print(isinstance(string, str))

try:
    a = 18
    b = 0
    print('Linha 1')
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('NameError')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('Continuar')
