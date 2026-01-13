import math

n = int(input("Digite um número:"))
a = n * 2
s = n * 3
b = n  ** (1/2)
print('O dobro de {} vale {}'.format(n,a))
print('O triplo de {} vale {}'.format(n,s))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n,math.sqrt(n)))