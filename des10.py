real = float(input('Quanto de dinheiro tem na carteira? R$: '))
dolar = real / 3.27
print('Com R${} voce pode comprar U$${:.2f}'.format(real, dolar))