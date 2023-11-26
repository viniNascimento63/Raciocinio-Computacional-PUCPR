import json

def menu():
    
    while True:
        try:
            # Menu principal do sistema
            print('\nMenu principal:'
                '\n(1) Estudantes'
                '\n(2) Professores'
                '\n(3) Disciplinas'
                '\n(4) Turmas'
                '\n(5) Matrículas'
                '\n(0) Sair')
            
            entrada1 = int(input('\n# Digite o número da opção desejada: '))
            if entrada1 < 0 or entrada1 > 5:
                print('# Opção inválida, Tente novamente.')
                # sleep(1.5)
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            # sleep(2)
            continue

    if entrada1 == 0:
        print('# Opção selecionada: (0) Sair'
              '\n# Você saiu.') 
        return entrada1
    elif entrada1 == 1:
        print('# Opção selecionada: (1) Estudantes')
    elif entrada1 == 2:
        print('# Opção selecionada: (2) Professores ')
    elif entrada1 == 3:
        print('# Opção selecionada: (3) Disciplinas')
    elif entrada1 == 4:
        print('# Opção selecionada: (4) Turmas ')
    else:    
        print('# Opção selecionada: (5) Matrículas')

    # Menu de operações
    while True:
        try:
            print('\n# Menu de operações:'
                    '\n(1) Incluir'
                    '\n(2) Listar'
                    '\n(3) Editar'
                    '\n(4) Excluir'
                    '\n(0) Voltar para o menu principal')
            
            entrada2 = int(input('\n# Digite o número da opção desejada: '))
            if entrada2 < 0 or entrada2 > 4:
                print('# Opção inválida! Tente novamente.')
                continue
            break
        except ValueError:
            print('# Valor inválido! Digite apenas valores numéricos.')
            # sleep(2)
            continue 

    # VOLTAR AO MENU PRINCIPAL
    if entrada2 == 0:
        print('# Opção selecionada: Voltar ao menu principal')
        
    # ADICIONAR ITENS NA LISTA
    elif entrada2 == 1:
        incluir(entrada1)
        
    # LISTAR
    elif entrada2 == 2:
        print('# Opção selecionada: 2. Listar')
        listar(entrada1)
                
    # EDITAR INFORMAÇÕES
    elif entrada2 == 3:
        listar(entrada1)
        editar(entrada1)

    # EXCLUIR
    elif entrada2 == 4:
        listar(entrada1)
        alunos = exluir_aluno(alunos)


def incluir(entrada):

    print('# Opção selecionada: 1. Incluir')

    # Incluir estudante
    if entrada == 1:
        alunos = []
        while True:
            codigo = int(input('\n# Informe o código do estudante: '))
            nome = input('# Informe o nome do estudante: ')
            cpf = input('# Informe o CPF do estudante (sem pontos ou espaços): ')

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
                salvar_dados(alunos, 'estudantes')
                return alunos
    
    # Incluir professores
    if entrada == 2:
        
        professores = []
        while True:
            codigo = int(input('\n# Informe o código do(a) professor(a): '))
            nome = input('# Informe o nome do(a) professor(a): ')
            cpf = input('# Informe o CPF do(a) professor(a) (sem pontos ou espaços): ')

            professor = {
                'Código': codigo,
                'Nome': nome,
                'CPF': cpf
            }

            professores.append(professor)

            # sleep(1.5)
            print(f'\n# Professor(a) {nome} adicionado(a) com sucesso!')

            while True:
                entrada = input('\n# Incluir mais professores (s/n)? ')
                if entrada.lower() != 's' and entrada.lower() != 'n':
                    print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                    continue
                else:
                    break
            
            if entrada.lower() == 'n':
                salvar_dados(professores, 'professores')
                return professores

    # Incluir disciplinas
    if entrada == 3:
        disciplinas = []
        while True:
            codigo = int(input('\n# Informe o código da disiciplina: '))
            nome = input('# Informe o nome da disciplina: ')

            disciplina = {
                'Código': codigo,
                'Nome': nome
            }

            disciplinas.append(disciplina)

            print(f'\n# Disciplina {nome} adicionada com sucesso!')

            while True:
                entrada = input('\n# Incluir mais disciplinas (s/n)? ')
                if entrada.lower() != 's' and entrada.lower() != 'n':
                    print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                    continue
                else:
                    break
            
            if entrada.lower() == 'n':
                salvar_dados(disciplinas, 'disciplinas')
                return disciplinas

    # Incluir turmas
    if entrada == 4:
        turmas = []
        while True:
            codigo = int(input('\n# Informe o código da turma: '))
            cod_prof = int(input('# Informe o código do(a) professor(a) associado à turma: '))
            cod_disciplina = int(input('\n# Informe o código da disiciplina associado à turma: '))

            turma = {
                'Código': codigo,
                'Código do professor': cod_prof,
                'Código da disciplina': cod_disciplina
            }

            turmas.append(turma)

            print(f'\n# Turma {nome} adicionada com sucesso!')

            while True:
                entrada = input('\n# Incluir mais turmas (s/n)? ')
                if entrada.lower() != 's' and entrada.lower() != 'n':
                    print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                    continue
                else:
                    break
            
            if entrada.lower() == 'n':
                salvar_dados(turmas, 'turmas')
                return turmas

    # Incluir matérias
    if entrada == 5:
        matriculas = []
        while True:
            cod_turma = int(input('\n# Informe o código da turma: '))
            cod_estudante = int(input('\n# Informe o código do(a) estudante: '))

            matricula = {
                'Código da turma': cod_turma,
                'Código do(a) estudante': cod_estudante
            }

            matriculas.append(matricula)

            print(f'\n# Matrícula {codigo} adicionada com sucesso!')

            while True:
                entrada = input('\n# Incluir mais matrículas (s/n)? ')
                if entrada.lower() != 's' and entrada.lower() != 'n':
                    print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                    continue
                else:
                    break
            
            if entrada.lower() == 'n':
                salvar_dados(matriculas, 'matriculas')
                return matriculas
            

def listar(entrada):

    
    if entrada == 1:
        nome_arquivo = 'estudantes'
    elif entrada == 2:
        nome_arquivo = 'professores'
    elif entrada == 3:
        nome_arquivo = 'disciplinas'
    elif entrada == 4:
        nome_arquivo = 'turmas'
    else:
        nome_arquivo = 'matriculas'

    dados_recuperados = recuperar_dados(nome_arquivo)
    
    if len(dados_recuperados) > 0:
        print(f'\nListagem:')
        for item in dados_recuperados:
            print(f'- {item}')
    else:
        print('# Não há itens cadastrados :(')
    
    return None


def editar(entrada):

    print('\n# Opção selecionada: 3. Editar')

    # Editar estudantes
    if entrada == 1:

        listar(entrada)
        lista_recuperada = recuperar_dados('estudantes')

        cod_estudante = int(input('\n# Digite o código do estudante para editar as informações: '))
        print('Estudante selecionado!')

        for indice, dicionario in enumerate(lista_recuperada):

            # Verifica se a entrada é o valor de uma chave no dicionário atual
            if cod_estudante in dicionario.values():

                # Recebe as novas informações do estudante
                codigo = int(input('\n# Atualize o código do estudante: '))
                nome = input('# Digite o nome do estudante: ')
                cpf = input('# Digite o CPF do estudante (sem pontos ou espaços): ')

                # Um novo dicionario recebe as informações atualizadas
                estudante = {
                    "Código": codigo,
                    "Nome": nome,
                    "CPF": cpf
                }

                # Substitui os dados antigos do estudante pelos novos
                lista_recuperada[indice] = estudante

                # Escreve os dados atualizados no arquivo 'estudantes.json'
                salvar_dados(lista_recuperada, 'estudantes')

                print(f'\n# Informações de {estudante["Nome"]} atualizadas com sucesso!')
            else:
                pass
    
    # Editar professores
    elif entrada == 2:
        pass

    # Editar disciplinas
    elif entrada == 3:
        pass

    # Editar turmas
    elif entrada == 4:
        pass

    # Editar matrículas
    else:
        pass


    return None


def exluir_aluno(lista_alunos):
    print('# Opção selecionada: 4. Excluir')
    listar()

    entrada = int(input('\n# Digite o código do estudante a ser exluído: '))
    for dicionario in lista_alunos:
        # Verifica se a entrada é uma chave no dicionário atual
        if entrada in dicionario.values():
            print(f'# Estudante {dicionario.get("Nome")} removido(a) com sucesso!')
            lista_alunos.remove(dicionario)
        else:
            pass

    return lista_alunos


def salvar_dados(dados, nome_arquivo):

    lista = recuperar_dados(nome_arquivo)
    
    for dicionario in dados:
        #if dicionario in lista:
            #continue
        lista.append(dicionario)

    # Escreve no arquivo os dados
    with open(nome_arquivo + '.json', "w", encoding='utf-8') as arquivo: 
        json.dump(lista, arquivo)
        arquivo.close()
    return None


def recuperar_dados(nome_arquivo):
    try:
        with open(nome_arquivo + '.json', 'r', encoding='utf-8') as arquivo:
            dados_recuperados = json.load(arquivo)
            arquivo.close()
        return dados_recuperados
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existe, retorna uma lista vazia
        return []
    
