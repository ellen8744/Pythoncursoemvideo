print("======= LOJAS DELUXE =======")
preco=float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENT0
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opção= int(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelado em 2x de R${:.2f}sem juros'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
     total = 0
     print('OPÇÃO INVÁLIDA de pagamento.Tente novamente! ')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preco, total))




