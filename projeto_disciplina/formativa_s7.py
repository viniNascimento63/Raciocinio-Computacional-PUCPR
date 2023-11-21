# Vinícius da Silva do Nascimento

from time import sleep
import funcoes

alunos = []
print('\nBem-vindo(a) ao Sistema PUC!')

while True:
    sleep(1.5)
    entrada = funcoes.menu_principal()
    
    sleep(1.5)
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

    sleep(1.5)
    entrada = funcoes.menu_operacoes()

    sleep(1.5)

    # VOLTAR AO MENU PRINCIPAL
    if entrada == 0:
        print('# Opção selecionada: Voltar ao menu principal')
        continue

    # ADICIONAR ESTUDANTES NA LISTA
    elif entrada == 1:
        alunos = funcoes.incluir_estudante(alunos)

    # MOSTRAR LISTA DE ESTUDANTES
    elif entrada == 2:
        print('# Opção selecionada: 2. Listar')
        alunos = funcoes.mostrar_lista_estudantes(alunos)

    # EDITAR INFORMAÇÕES DE ESTUDANTE
    elif entrada == 3:
        funcoes.mostrar_lista_estudantes(alunos)
        alunos = funcoes.editar_informacao_aluno(alunos)

    # EXCLUIR ESTUDANTE
    elif entrada == 4:
        alunos = funcoes.exluir_aluno(alunos)

sleep(1.5)
print('\n# Fim da aplicação.')