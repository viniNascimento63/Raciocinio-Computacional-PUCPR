from time import sleep

print('\nBem-vindo(a) ao Sistema PUC!')

while True:
    sleep(1.5)
    selecao = 0
    while True:
        try:
            # Menu principal do sistema
            print('\nMenu principal:'
                  '\n(1) Estudantes'
                  '\n(2) Disciplinas'
                  '\n(3) Professores'
                  '\n(4) Turmas'
                  '\n(5) Matrículas'
                  '\n(0) Sair')
            selecao = int(input('\n# Digite o número da opção desejada: '))
            if selecao < 0 or selecao > 5:
                print('# Opção inválida, Tente novamente.')
                sleep(1.5)
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            sleep(2)
            continue
    sleep(1.5)

    if selecao == 0:
        print('# Opção selecionada: (0) Sair'
              '\n# Você saiu.')
        break
    elif selecao == 1:
        print('# Opção selecionada: (1) Estudantes')
    elif selecao == 2:
        print('# Opção selecionada: (2) Disciplinas ')
    elif selecao == 3:
        print('# Opção selecionada: (3) Professores')
    elif selecao == 4:
        print('# Opção selecionada: (4) Turmas ')
    else:
        print('# Opção selecionada: (5) Matrículas')

    sleep(1.5)
    while True:
        try:
            print('\n# Menu de operações:'
                  '\n(1) Incluir'
                  '\n(2) Listar'
                  '\n(3) Atualizar'
                  '\n(0) Voltar para o menu principal')
            selecao = int(input('\n# Digite o número da opção desejada: '))
            if selecao < 0 or selecao > 3:
                print('# Opção inválida! Tente novamente.')
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            sleep(2)
            continue

    sleep(1.5)

    if selecao == 0:
        print('# Opção selecionada: Voltar ao menu principal')
        continue
    elif selecao == 1:
        print('# Opção selecionada: 1. Incluir')
        break
    elif selecao == 2:
        print('# Opção selecionada: 2. Listar')
        break
    else:
        print('# Opção selecionada: 3. Atualizar')
        break

sleep(1.5)
print('\n# Fim da aplicação.')
