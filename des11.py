n = float(input('Qual a largura da sua parede? : '))
m = float(input('Qual a altura da sua parede? : '))
area = n*m
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(n,m, area))
print('Para pintar essa parede, voce precisará de {}L de tinta.'.format(area/2))