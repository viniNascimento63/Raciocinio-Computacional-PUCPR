print('\n# Qual é o tipo do triângulo?\n')

lado1 = int(input('Informe o tamanho do lado 1: '))
lado2 = int(input('Informe o tamanho do lado 2: '))
lado3 = int(input('Informe o tamanho do lado 3: '))

# Para ser triângulo:
if (lado1 + lado2 > lado3) or (lado1 + lado3 > lado2) or (lado2 + lado3 > lado1):
    # Para ser equilátero:
    if lado1 == lado2 == lado3:
        print('\n# Triângulo equilátero.')
    # Para ser isósceles:
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('\n# Triângulo isósceles.')
    # Escaleno:
    else:
        print('\n# Triângulo escaleno.')
else:
    print('A figura não é um triângulo!')
