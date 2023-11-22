import json
import pickle

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
        salvar_lista_estudantes(lista_alunos, )

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
            

def mostrar_lista_estudantes(lista_alunos):

    if len(lista_alunos) > 0:
        print(f'\nLista de alunos:')
        for aluno in lista_alunos:
            print(f'- {aluno}')
    else:
        print('# Não há estudantes cadastrados :(')

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
    mostrar_lista_estudantes(lista_alunos)

    entrada = int(input('\n# Digite o código do estudante a ser exluído: '))
    for dicionario in lista_alunos:
        # Verifica se a entrada é uma chave no dicionário atual
        if entrada in dicionario.values():
            print(f'# Estudante {dicionario.get("Nome")} removido(a) com sucesso!')
            lista_alunos.remove(dicionario)
        else:
            pass

    return lista_alunos


def salvar_lista_estudantes(lista_alunos):
    with open("dados_alunos.json", "a", encoding="utf-8") as arquivo:
        json.dump(lista_alunos, arquivo)   

    return None

def recuperar_dados_estudantes():
    with open("dados_alunos.json", "r", encoding="UTF-8") as arquivo:
        dados_lidos = json.load(arquivo)
    print(dados_lidos)
    return None

recuperar_dados_estudantes()