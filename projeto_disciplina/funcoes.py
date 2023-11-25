import json

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
        

def incluir_estudante():
    lista_alunos = []
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
            salvar_dados(lista_alunos, 'dados_alunos')
            return lista_alunos
            

def listar(nome_arquivo=str):

    dados_recuperados = recuperar_dados(nome_arquivo)
    
    if len(dados_recuperados) > 0:
        print(f'\nListagem:')
        for item in dados_recuperados:
            print(f'- {item}')
    else:
        print('# Não há itens cadastrados :(')
    
    return None


def editar_informacao_aluno(lista_alunos):

    print('\n# Opção selecionada: 2. Editar')

    entrada = int(input('\n# Digite o código do estudante para editar as informações: '))
    print('Estudante selecionado!')

    for indice, dicionario in enumerate(lista_alunos):

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
            lista_alunos[indice] = estudante

            print(f'\n# Informações de {dicionario["Nome"]} atualizadas com sucesso!')
        else:
            pass

    return lista_alunos


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
    
