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
        editar(entrada1, entrada2)

    # EXCLUIR
    elif entrada2 == 4:
        print('\n# Opção selecionada: 4. Excluir')
        dados = listar(entrada1)
        excluir(entrada1, dados)


def incluir(entrada):

    print('# Opção selecionada: 1. Incluir')

    # Incluir estudante
    if entrada == 1:
        alunos = []
        while True:
            codigo = int(input('\n# Informe o código do estudante: '))
            
            # Verifica se o código já está presente na lista de alunos
            if any(estudante['Código'] == codigo for estudante in alunos):
                print('\n# Estudante já cadastrado! Insira um novo código')
                continue  # Retorna ao início do loop para pedir um novo código

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
                salvar_dados(entrada, alunos, 'estudantes')
                return alunos
    
    # Incluir professores
    if entrada == 2:
        
        professores = []
        while True:
            codigo = int(input('\n# Informe o código do(a) professor(a): '))
            
            # Verifica se o código já está presente na lista de professores
            if any(professor['Código'] == codigo for professor in professores):
                print('\n# Professor(a) já cadastrado(a)! Insira um novo código')
                continue  # Retorna ao início do loop para pedir um novo código

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
                salvar_dados(entrada, professores, 'professores')
                return professores

    # Incluir disciplinas
    if entrada == 3:
        disciplinas = []
        while True:
            codigo = int(input('\n# Informe o código da disciplina: '))

            # Verifica se o código já está presente na lista de disciplinas
            if any(disciplina['Código'] == codigo for disciplina in disciplinas):
                print('\n# Disciplina já cadastrada! Insira um novo código')
                continue  # Retorna ao início do loop para pedir um novo código

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
                salvar_dados(entrada, disciplinas, 'disciplinas')
                return disciplinas

    # Incluir turmas
    if entrada == 4:
        # Para adicionar uma turma é necessário que haja professores e disciplinas
        prof = recuperar_dados('professores')
        disc = recuperar_dados('disciplinas')

        if len(prof) > 0 and len(disc) > 0:

            turmas = []
            while True:
                codigo = int(input('\n# Informe o código da turma: '))

                # Verifica se o código já está presente na lista de turmas
                if any(turma['Código_turma'] == codigo for turma in turmas):
                    print('\n# Turma já cadastrada! Insira um novo código')
                    continue  # Retorna ao início do loop para pedir um novo código

                print('\n# Professores')
                listar(2)
                cod_prof = int(input('\n# Informe o código do(a) professor(a) associado à turma: '))

                print('\n# Disciplinas')
                listar(3)
                cod_disciplina = int(input('\n# Informe o código da disiciplina associado à turma: '))

                turma = {
                    'Código_turma': codigo,
                    'Código_professor': cod_prof,
                    'Código_disciplina': cod_disciplina
                }

                turmas.append(turma)

                print(f'\n# Turma {codigo} adicionada com sucesso!')

                while True:
                    entrada = input('\n# Incluir mais turmas (s/n)? ')
                    if entrada.lower() != 's' and entrada.lower() != 'n':
                        print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                        continue
                    else:
                        break
                
                if entrada.lower() == 'n':
                    salvar_dados(entrada, turmas, 'turmas')
                    return turmas
        
        elif len(prof) == 0 and len(disc) > 0:
            print('\n# Não é possível adicionar turmas pois não há professores cadastrados.'
                  '\n# Por favor, adicione professores ao sistema!')
            incluir(2)
            
        elif len(disc) == 0 and len(prof) > 0:
            print('\n# Não é possível adicionar turmas pois não há disciplinas cadastradas.'
                  '\n# Por favor, adicione disciplinas ao sistema!')
            incluir(3)
        
        else:
            print('\n# Não é possível adicionar turmas pois não há professorse e disciplinas cadastrados.'
                  '\n# Por favor, adicione professores e disciplinas ao sistema!')

    # Incluir matrículas
    if entrada == 5:
        matriculas = []
        while True:
            print('\n# Estudantes')
            listar(1)
            cod_estudante = int(input('\n# Informe o código do(a) estudante: '))

            print('Turmas')
            listar(4)
            cod_turma = int(input('\n# Informe o código da turma: '))

            matricula = {
                'Código_estudante': cod_estudante,
                'Turma': cod_turma
            }

            matriculas.append(matricula)
            salvar_dados(entrada, matriculas, 'matriculas')

            print(f'\n# Matrícula adicionada com sucesso!')

            while True:
                entrada = input('\n# Incluir mais matrículas (s/n)? ')
                if entrada.lower() != 's' and entrada.lower() != 'n':
                    print("\n# Valor inválido. Digite 's' ou 'n' para continuar.")
                    continue
                else:
                    break
            
            if entrada.lower() == 'n':
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
    
    # Imprimindo os dados no terminal
    if len(dados_recuperados) > 0:
        print(f'\nListagem:')
        for item in dados_recuperados:
            print(f'- {item}')
    else:
        print('# Não há itens cadastrados :(')
    
    return dados_recuperados


def editar(entrada1, entrada2):

    print('\n# Opção selecionada: 3. Editar')

    # Editar estudantes
    if entrada1 == 1:

        listar(entrada1)
        lista_recuperada = recuperar_dados('estudantes')

        cod_estudante = int(input('\n# Digite o código do(a) estudante para editar as informações: '))
        print('Estudante selecionado!')

        for indice, dicionario in enumerate(lista_recuperada):

            # Verifica se a entrada é o valor de uma chave no dicionário atual
            if cod_estudante in dicionario.values():

                # Recebe as novas informações do estudante
                codigo = int(input('\n# Atualize o código do(a) estudante: '))
                nome = input('# Digite o nome do(a) estudante: ')
                cpf = input('# Digite o CPF do(a) estudante (sem pontos ou espaços): ')

                # Um novo dicionario recebe as informações atualizadas
                estudante = {
                    "Código": codigo,
                    "Nome": nome,
                    "CPF": cpf
                }

                # Substitui os dados antigos do estudante pelos novos
                lista_recuperada[indice] = estudante

                # Escreve os dados atualizados no arquivo 'estudantes.json'
                salvar_dados(entrada2, lista_recuperada, 'estudantes')

                print(f'\n# Informações de {estudante["Nome"]} atualizadas com sucesso!')
            else:
                pass
    
    # Editar professores
    elif entrada1 == 2:
        
        lista_recuperada = listar(entrada1)
        
        cod_prof = int(input('\n# Digite o código do(a) professar(a) para editar as informações: '))
        print(f'Professor(a) de código {cod_prof} selecionado(a)!')

        for indice, dicionario in enumerate(lista_recuperada):

            # Verifica se a entrada é o valor de uma chave no dicionário atual
            if cod_prof in dicionario.values():

                # Recebe as novas informações do professor
                codigo = int(input('\n# Atualize o código do(a) professor(a): '))
                nome = input('# Digite o nome do(a) professor(a): ')
                cpf = input('# Digite o CPF do(a) professor(a) (sem pontos ou espaços): ')

                # Um novo dicionario recebe as informações atualizadas
                professor = {
                    "Código": codigo,
                    "Nome": nome,
                    "CPF": cpf
                }

                # Substitui os dados antigos do professor pelos novos
                lista_recuperada[indice] = professor

                # Sobrescreve os dados atualizados no arquivo 'professores.json'
                salvar_dados(entrada2, lista_recuperada, 'professores')

                print(f'\n# Informações de {professor["Nome"]} atualizadas com sucesso!')
            else:
                # Código não do professor não encontrado, tente novamente
                break

    # Editar disciplinas
    elif entrada1 == 3:
        lista_recuperada = listar(entrada1)
        
        cod_disciplina = int(input('\n# Digite o código da disciplina para editar as informações: '))
        print(f'Disciplina de código {cod_disciplina} selecionada!')

        for indice, dicionario in enumerate(lista_recuperada):

            # Verifica se a entrada é o valor de uma chave no dicionário atual
            if cod_disciplina in dicionario.values():

                # Recebe as novas informações da disciplina
                cod_disciplina = int(input('\n# Atualize o código da disciplina: '))
                nome = input('# Digite o nome da disciplina: ')

                # Um novo dicionario recebe as informações atualizadas
                disciplina = {
                    "Código": cod_disciplina,
                    "Nome": nome
                }

                # Substitui os dados antigos da disciplina pelos novos
                lista_recuperada[indice] = disciplina

                # Sobrescreve os dados atualizados no arquivo 'professores.json'
                salvar_dados(entrada2, lista_recuperada, 'disciplinas')

                print(f'\n# Informações de {disciplina["Nome"]} atualizadas com sucesso!')
            else:
                # Código não da disciplina não encontrado, tente novamente
                break

    # Editar turmas
    elif entrada1 == 4:
        lista_recuperada = listar(entrada1)
        
        cod_turma = int(input('\n# Digite o código da turma para editar as informações: '))
        print(f'Disciplina de código {cod_turma} selecionada!')

        for indice, dicionario in enumerate(lista_recuperada):

            # Verifica se a entrada é o valor de uma chave no dicionário atual
            if cod_turma in dicionario.values():

                # Recebe as novas informações da turma
                cod_turma = int(input('\n# Atualize o código da turma: '))
                cod_prof = int(input('\n# Atualize o código do(a) professor(a): '))
                cod_disciplina = int(input('\n# Atualize o código da disciplina: '))
                

                # Um novo dicionario recebe as informações atualizadas
                turma = {
                    "Turma": cod_turma,
                    "Código_professor": cod_prof,
                    "Código_disciplina": cod_disciplina
                }

                # Substitui os dados antigos da turma pelos novos
                lista_recuperada[indice] = turma

                # Sobrescreve os dados atualizados no arquivo 'turmas.json'
                salvar_dados(entrada2, lista_recuperada, 'turmas')

                print(f'\n# Informações de {turma["Turma"]} atualizadas com sucesso!')
            else:
                # Código não da turma não encontrado, tente novamente
                break

    # Editar matrículas
    else:

        lista_recuperada = listar(entrada1)
        
        cod_estudante = int(input('\n# Digite o código do(a) estudante para editar as informações de "Matrículas": '))
        print(f'Estudante de código {cod_estudante} selecionada!')

        for indice, dicionario in enumerate(lista_recuperada):

            # Verifica se a entrada é o valor de uma chave no dicionário atual
            if cod_turma in dicionario.values():

                # Recebe as novas informações da turma
                cod_estudante = int(input('\n# Atualize o código do(a) estudante(a): '))
                cod_turma = int(input('\n# Atualize o código da turma: '))

                # Um novo dicionario recebe as informações atualizadas
                matricula = {
                    "Código_estudante": cod_estudante,
                    "Turma": cod_turma
                }

                # Substitui os dados antigos da turma pelos novos
                lista_recuperada[indice] = matricula

                # Sobrescreve os dados atualizados no arquivo 'matriculas.json'
                salvar_dados(entrada2, lista_recuperada, 'matriculas')

                print(f'\n# Informações de {matricula["Código_estudante"]} atualizadas com sucesso!')
            else:
                # Código não da matricula não encontrado, tente novamente
                break

    return None


def excluir(entrada, dados):
    
    while True:

        # Excluir estudante
        if entrada == 1:
            
            for indice, dicionario in enumerate(dados):
                cod = int(input('\n# Digite o código do(a) estudante a ser exluído(a): '))
                # Verifica se a entrada é uma chave no dicionário atual
                if cod in dicionario.values():
                    print(f'# Estudante removido(a) com sucesso!')
                    dados.remove(dicionario)
                    salvar_dados(3, dados, 'estudantes')
                    listar(entrada)
                    return dados
                elif indice == (len(dados) - 1):
                    print('\n# O código informado não pertence a nenhum estudante da lista. Tente novamente!')
                    break
                else:
                    continue 
        
        # Excluir professor
        elif entrada == 2:
            cod = int(input('\n# Digite o código do(a) professor(a) a ser exluído(a): '))
           
            for dicionario in dados:
                # Verifica se a entrada é uma chave no dicionário atual
                if cod in dicionario.values():
                    print(f'# Professor(a) removido(a) com sucesso!')
                    dados.remove(dicionario)
                    listar(dados)
                    salvar_dados(3, dados, 'professores')
                    return dados
                elif indice == (len(dados) - 1):
                    print('\n# O código informado não pertence a nenhum professor da lista. Tente novamente!')
                    break
                else:
                    continue 
        
        # Excluir disciplinas
        elif entrada == 3:
            cod = int(input('\n# Digite o código da disciplina a ser exluída: '))
            for dicionario in dados:
                # Verifica se a entrada é uma chave no dicionário atual
                if cod in dicionario.values():
                    print(f'# Disciplina removida com sucesso!')
                    dados.remove(dicionario)
                    listar(dados)
                    salvar_dados(3, dados, 'disciplinas')
                    return dados
                elif indice == (len(dados) - 1):
                    print('\n# O código informado não pertence a nenhuma disciplina da lista. Tente novamente!')
                    break
                else:
                    continue 
        
        # Excluir turmas
        elif entrada == 4:
            cod = int(input('\n# Digite o código da turma a ser exluída: '))
            for dicionario in dados:
                # Verifica se a entrada é uma chave no dicionário atual
                if cod in dicionario.values():
                    print(f'# Turma removida com sucesso!')
                    dados.remove(dicionario)
                    listar(dados)
                    salvar_dados(3, dados, 'turmas')
                    return dados
                elif indice == (len(dados) - 1):
                    print('\n# O código informado não pertence a nenhuma turma da lista. Tente novamente!')
                    break
                else:
                    continue 
        
        # Excluir matrículas
        else: 
            cod = int(input('\n# Digite o código da matrícula a ser exluída: '))
            for dicionario in dados:
                # Verifica se a entrada é uma chave no dicionário atual
                if cod in dicionario.values():
                    print(f'# Matrícula removida com sucesso!')
                    dados.remove(dicionario)
                    listar(dados)
                    salvar_dados(3, dados, 'matriculas')
                    return dados
                elif indice == (len(dados) - 1):
                    print('\n# O código informado não pertence a nenhuma matrícula da lista. Tente novamente!')
                    break
                else:
                    continue 


def salvar_dados(entrada, dados, nome_arquivo):

    # Escreve os dados novos no arquivo (1)
    if entrada == 1:
        lista = recuperar_dados(nome_arquivo)

        # Adiciona cada novo dicionário à lista
        for dicionario in dados:
            lista.append(dicionario)

        with open(nome_arquivo + '.json', "w", encoding='utf-8') as arquivo: 
            json.dump(dados, arquivo)
            arquivo.close()
        return None
    
    # Sobrescreve os dados recebidos no arquivo (3)
    else:
        with open(nome_arquivo + '.json', "w", encoding='utf-8') as arquivo: 
            json.dump(dados, arquivo)
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
    
