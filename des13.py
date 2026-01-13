salario = float(input("Qual é o salário do fucionário? R$"))
novo = salario + (salario*15/100)
print('Um fucionário que ganhava R${},com 15% de aumento,passa a receber R${:.2f}'.format(salario, novo))