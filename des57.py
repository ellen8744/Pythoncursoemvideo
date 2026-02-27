sexo = str(input('Informe o sexo: [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos.Por favor ,informa seu sexo: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso!'.format(sexo))