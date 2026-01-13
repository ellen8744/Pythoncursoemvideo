import math

a=float(input('Comprimento do cateto oposto: '))
b=float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(a,b)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))