r1= float(input('Primeiro triangulo: '))
r2 = float(input('Segundo triangulo: '))
r3 = float(input('Terceiro triangulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1:
    print('Os segmentos acima podem formar um triangulo', end='')
if r1 == r2 == r3:
        print('EQUILATERO')
elif r1 != r2 != r3 != r1:
    print('ESCALENO')
else:
    print("ISOSCELES")
