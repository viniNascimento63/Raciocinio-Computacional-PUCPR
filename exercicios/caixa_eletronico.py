print('Notas disponíveis: R$ 1, 5, 10, 50, 100')
valor = float(input('Digite o valor do saque: R$ ').replace(',', '.'))
resto = cem = cinq = dez = cinc = um = 0

if valor < 10:
    print('Valor mínimo para saques: R$ 10,00')
elif valor > 600:
    print('Valor máximo para saques: R$ 600,00')
elif True:
    if valor >= 100:
        resto = valor % 100
    if resto >= 50:
