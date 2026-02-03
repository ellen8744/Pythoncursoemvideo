salario=int(input('Qual é o salário do fucionário? R$'))
if salario <= 1250:
    novo_salario = salario * 15/100
else:
    novo_salario = salario * 10/100
    novo_salario = salario + novo_salario
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora".format(salario,novo_salario))