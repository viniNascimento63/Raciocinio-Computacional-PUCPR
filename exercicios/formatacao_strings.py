nome = "Vinícius"
mensagem = "Olá %s, tudo certo?" % nome
print(mensagem)

idade = "Meu avô faz %d anos hoje. Parabéns vovô" % 95
print(idade)

presente = 'Estou sem um R$ %.2f para comprar um presente!' % 1
print(presente)

data = 'Hoje é dia %d/%d/%d às %d:%d horas, viajei no tempo!' % (2, 10, 2023, 17, 56)
print(data)

dados = 'Formatos int = {}, float = {} e str = {}'.format(8, 7.7, 'Olá')
print(dados)

# Invertendo as informações através dos índices
dados1 = 'Formatos int = {2}, float = {1} e str = {0}'.format(8, 7.7, 'Olá')
print(dados1)
