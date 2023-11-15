# Vinícius da Silva do Nascimento

from time import sleep
import funcoes

alunos = []
print('\nBem-vindo(a) ao Sistema PUC!')

while True:
    # sleep(1.5)
    entrada = funcoes.menu_principal()
    
    # sleep(1.5)
    if entrada == 0:
        print('# Opção selecionada: (0) Sair'
              '\n# Você saiu.')
        break
    elif entrada == 1:
        print('# Opção selecionada: (1) Estudantes')
    elif entrada == 2:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (2) Disciplinas ')
    elif entrada == 3:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (3) Professores')
    elif entrada == 4:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (4) Turmas ')
    else:
        print('# Em DESENVOLVIMENTO...')
        continue
        # print('# Opção selecionada: (5) Matrículas')

    # sleep(1.5)
    entrada = funcoes.menu_operacoes()

    # sleep(1.5)

    # VOLTAR AO MENU PRINCIPAL
    if entrada == 0:
        print('# Opção selecionada: Voltar ao menu principal')
        continue

    # ADICIONAR ESTUDANTES NA LISTA
    elif entrada == 1:
        alunos = funcoes.incluir_estudante(alunos)

    # MOSTRAR LISTA DE ESTUDANTES
    elif entrada == 2:
        alunos = funcoes.mostrar_lista_estudantes(alunos)

    # EDITAR INFORMAÇÕES DE ESTUDANTE
    elif entrada == 3:
        print('\n# Opção selecionada: 2. Editar')

        # MOSTRA LISTA DE ESTUDANTES
        funcoes.mostrar_lista_estudantes(alunos)

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
    elif entrada == 4:
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
