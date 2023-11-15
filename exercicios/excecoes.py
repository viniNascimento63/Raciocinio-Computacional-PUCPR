while True:
    try:
        num = int(input('Digite um número: '))
        break
    except ValueError:
        print('O valor digitado inválido!')
print(f'Número ({num}) validado com sucesso!')
