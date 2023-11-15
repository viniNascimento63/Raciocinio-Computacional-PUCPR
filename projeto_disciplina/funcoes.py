def menu_principal():
    
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
            

            entrada = int(input('\n# Digite o número da opção desejada: '))
            if entrada < 0 or entrada > 5:
                print('# Opção inválida, Tente novamente.')
                # sleep(1.5)
                continue
            return entrada
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            # sleep(2)
            continue
      


def menu_operacoes():
    while True:
        try:
            print('\n# Menu de operações:'
                    '\n(1) Incluir'
                    '\n(2) Listar'
                    '\n(3) Editar'
                    '\n(4) Excluir'
                    '\n(0) Voltar para o menu principal')
            
            entrada = int(input('\n# Digite o número da opção desejada: '))
            if entrada < 0 or entrada > 4:
                print('# Opção inválida! Tente novamente.')
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            # sleep(2)
            continue 
    return entrada
        

def incluir_estudante(lista_alunos):

    print('# Opção selecionada: 1. Incluir')

    while True:
        codigo = int(input('\n# Informe o código do estudante: '))
        nome = input('# Informe o nome do estudante: ')
        cpf = int(input('# Informe o CPF do estudante (sem pontos ou espaços): '))

        estudante = {
            'Código': codigo,
            'Nome': nome,
            'CPF': cpf
        }

        lista_alunos.append(estudante)

        # sleep(1.5)
        print(f'\n# Estudante {nome} adicionado(a) com sucesso!')

        while True:
            entrada = input('\n# Incluir mais estudantes (s/n)? ')
            if entrada.lower() != 's' and entrada.lower() != 'n':
                print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                continue
            else:
                break

        if entrada.lower() == 'n':
            return lista_alunos
            break


def mostrar_lista_estudantes(lista_alunos):
    print('# Opção selecionada: 2. Listar')

    if len(lista_alunos) > 0:
        print(f'\nLista de alunos:')
        for aluno in lista_alunos:
            print(f'- {aluno}')
    else:
        print('# Não há estudantes cadastrados :(')

    return None

