turno = input('Em que turno trabalha?\n(manhã = M'
              '; tarde = T; noite = N): ')

if turno.lower() == 'm':
    print('Bom dia!')
elif turno.lower() == 't':
    print('Boa tarde!')
else:
    print('Boa noite!')
