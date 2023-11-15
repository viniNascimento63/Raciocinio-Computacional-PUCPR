salario = float(input('# Digite seu salário por favor R$ '))
if salario < 5000:
    abono = salario * 0.15
    print('Salário identificado R$ %.2f' % salario)
    print('Seu abono salarial é de R$ %.2f' % abono)
else:
    print('Salário identificado R$ %.2f' % salario)
    abono = salario * 0.1
    print('Seu abono salarial é de R$ %.2f' % abono)
