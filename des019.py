import random
a=str(input('Pimeiro aluno:'))
b=str(input('Segundo aluno:'))
c=str(input('Terceiro aluno:'))
d=str(input('Quarto aluno:'))
lista=[a,b,c,d]
escolhido=random.choice(lista)
print('O aluno escolido foi {}'.format(escolhido))