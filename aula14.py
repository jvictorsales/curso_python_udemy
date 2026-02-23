a = 'A'
b = 'B'
c = 1.14564

# string = 'a={}, b={}, c={:.2f}'
# string = 'b={1}, a={0}, a={0}, a={0}, c={2:.2f}'
string = 'b={nome_2}, a={nome_1}, a={nome_1}, a={nome_1}, c={nome_3:.2f}'
formato = string.format(nome_1 = a, nome_2 = b, nome_3 = c)

print(formato)
