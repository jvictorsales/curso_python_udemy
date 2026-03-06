# dir, hasattr e getattr em Python
string = 'João'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(string.upper())
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)