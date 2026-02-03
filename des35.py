print('-='*20)
print("Analisador de triangulos")
print("-="*20)
r1= float(input('Primeiro triangulo: '))
r2 = float(input('Segundo triangulo: '))
r3 = float(input('Terceiro triangulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos formam um triangulo')
else:
    print('Os segmentos NãO formam um triangulo')

