def menu_principal():
    print('\nMenu principal:'
          '\n(1) Estudantes'
          '\n(2) Disciplinas'
          '\n(3) Professores'
          '\n(4) Turmas'
          '\n(5) Matrículas'
          '\n(0) Sair')


def menu_operacoes():
    print('\n# Menu de operações:'
          '\n(1) Incluir'
          '\n(2) Listar'
          '\n(3) Editar'
          '\n(4) Excluir'
          '\n(0) Voltar para o menu principal')


def incluir_estudante(lista_estudantes):
    print('# Opção selecionada: 1. Incluir')
    alunos = lista_estudantes

    while True:
        codigo = int(input('\n# Informe o código do estudante: '))
        nome = input('# Informe o nome do estudante: ')
        cpf = int(input('# Informe o CPF do estudante (sem pontos ou espaços): '))

        estudante = {
            'Código': codigo,
            'Nome': nome,
            'CPF': cpf
        }

        alunos.append(estudante)

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
            break
    return None

def mostra_lista_estudantes(lista_alunos):
    print('# Opção selecionada: 2. Listar')

    if len(lista_alunos) > 0:
        print(f'\nLista de alunos:')
        for aluno in lista_alunos:
            print(f'- {aluno}')
    else:
        print('# Não há estudantes cadastrados :(')


mostra_lista_estudantes()