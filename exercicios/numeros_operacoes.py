num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operacao = input('Digite o símbolo da operação desejada (+, -, *, /): ')
res = int

if operacao == '+':
    res = num1 + num2
elif operacao == '-':
    res = num1 - num2
elif operacao == '*':
    res = num1 * num2
elif operacao == '/':
    res = num1 / num2
else:
    print('Operação inválida!')

print(f'\nOperação: {num1} {operacao} {num2} = {res}')
