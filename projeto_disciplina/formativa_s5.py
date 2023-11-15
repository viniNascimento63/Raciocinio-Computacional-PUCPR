# Vinícius da Silva do Nascimento

from time import sleep
import funcoes

alunos = []
print('\nBem-vindo(a) ao Sistema PUC!')

while True:
    # sleep(1.5)
    selecao = 0
    while True:
        try:
            # Menu principal do sistema
            funcoes.menu_principal()

            selecao = int(input('\n# Digite o número da opção desejada: '))
            if selecao < 0 or selecao > 5:
                print('# Opção inválida, Tente novamente.')
                # sleep(1.5)
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            # sleep(2)
            continue
    # sleep(1.5)

    if selecao == 0:
        print('# Opção selecionada: (0) Sair'
              '\n# Você saiu.')
        break
    elif selecao == 1:
        print('# Opção selecionada: (1) Estudantes')
    elif selecao == 2:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (2) Disciplinas ')
    elif selecao == 3:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (3) Professores')
    elif selecao == 4:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (4) Turmas ')
    else:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (5) Matrículas')

    # sleep(1.5)
    while True:
        try:
            print('\n# Menu de operações:'
                  '\n(1) Incluir'
                  '\n(2) Listar'
                  '\n(3) Editar'
                  '\n(4) Excluir'
                  '\n(0) Voltar para o menu principal')
            selecao = int(input('\n# Digite o número da opção desejada: '))
            if selecao < 0 or selecao > 4:
                print('# Opção inválida! Tente novamente.')
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            # sleep(2)
            continue

    # sleep(1.5)

    # VOLTAR AO MENU PRINCIPAL
    if selecao == 0:
        print('# Opção selecionada: Voltar ao menu principal')
        continue

    # ADICIONAR ESTUDANTES NA LISTA
    elif selecao == 1:
        funcoes.incluir_estudante(alunos)

    # MOSTRAR LISTA DE ESTUDANTES
    elif selecao == 2:
        print('# Opção selecionada: 2. Listar')
        if len(alunos) > 0:
            print(f'\nLista de alunos:')
            for aluno in alunos:
                print(f'- {aluno}')
        else:
            print('# Não há estudantes cadastrados :(')

    # EDITAR INFORMAÇÕES DE ESTUDANTE
    elif selecao == 3:
        print('\n# Opção selecionada: 2. Editar')

        # MOSTRA LISTA DE ESTUDANTES
        if len(alunos) > 0:
            print(f'\nLista de alunos:')
            for aluno in alunos:
                print(f'- {aluno}')
        else:
            print('# Não há estudantes cadastrados :(')

        entrada = int(input('\n# Digite o código do estudante para editar as informações: '))
        print('Estudante selecionado!')

        for indice, dicionario in enumerate(alunos):

            # Verifica se a entrada é uma chave no dicionário atual
            if entrada in dicionario.values():

                # Recebe as novas informações do estudante
                codigo = int(input('\n# Atualize o código do estudante: '))
                nome = input('# Digite o nome do estudante: ')
                cpf = int(input('# Digite o CPF do estudante (sem pontos ou espaços): '))

                # Um novo dicionario recebe as informações atualizadas
                estudante = {
                    "Código": codigo,
                    "Nome": nome,
                    "CPF": cpf
                }

                # Substitui os dados antigos do estudante pelos novos
                alunos[indice] = estudante

                print(f'# Informações de {dicionario["Nome"]} editadas com sucesso!')
            else:
                pass

    # EXCLUIR ESTUDANTE
    else:
        if len(alunos) > 0:
            print(f'\nLista de alunos:')
            for aluno in alunos:
                print(f'- {aluno}')
        else:
            print('# Não há estudantes cadastrados :(')

        entrada = int(input('\n# Digite o código do estudante a ser exluído: '))
        for dicionario in alunos:
            # Verifica se a entrada é uma chave no dicionário atual
            if entrada in dicionario.values():
                print(f'# Estudante {dicionario.get("Nome")} removido(a) com sucesso!')
                alunos.remove(dicionario)
            else:
                pass

# sleep(1.5)
print('\n# Fim da aplicação.')
