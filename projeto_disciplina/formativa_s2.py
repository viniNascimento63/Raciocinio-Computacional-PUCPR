from time import sleep

# Menu principal do sistema
print('\nBem-vindo(a) ao Sistema PUC!\n')
sleep(1.5)
print('Menu principal:'
      '\n1. Estudantes'
      '\n2. Disciplinas'
      '\n3. Professores'
      '\n4. Turmas'
      '\n5. Matrículas'
      '\nSair (s)')

selecao = input('\n# Escreva o número ou nome da opção desejada: ')
sleep(1.5)

if selecao.lower() == 'sair' or selecao.lower() == 's':
    print('# Opção selecionada: Sair')
elif selecao.lower() == 'estudantes' or selecao == '1':
    print('# Opção selecionada: 1. Estudantes')
elif selecao.lower() == 'disciplinas' or selecao == '2':
    print('# Opção selecionada: 2. Disciplinas ')
elif selecao.lower() == 'professores' or selecao == '3':
    print('# Opção selecionada: 3. Professores')
elif selecao.lower() == 'turmas' or selecao == '4':
    print('# Opção selecionada: 4. Turmas ')
elif selecao.lower() == 'matriculas' or selecao.lower() == 'matrículas' or selecao == '5':
    print('# Opção selecionada: 5. Matrículas')
else:
    print('# Opção inválida!')

sleep(1.5)
print('\n# Menu de operações:'
      '\n1. Incluir'
      '\n2. Listar'
      '\n3. Atualizar'
      '\nVoltar para o menu principal (s/n)')

selecao = input('\nEscreva o número ou nome da opção desejada: ')
sleep(1.5)

if selecao.lower() == 's':
    print('# Opção selecionada: Voltar ao menu principal')
elif selecao.lower() == '1' or selecao.lower() == 'incluir':
    print('# Opção selecionada: 1. Incluir')
elif selecao.lower() == '2' or selecao.lower() == 'listar':
    print('# Opção selecionada: 2. Listar')
elif selecao.lower() == '3' or selecao.lower() == 'atualizar':
    print('# Opção selecionada: 3. Atualizar')
else:
    print('Opção inválida!')

sleep(1.5)
print('\n# Fim da aplicação.')
