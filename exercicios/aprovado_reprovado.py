nota1 = float(input('Nota primeiro bimestre: '))
nota2 = float(input('Nota segundo bimestre: '))
nota3 = float(input('Nota terceiro bimestre: '))
nota4 = float(input('Nota quarto bimestre: '))
faltas = int(input('Número de faltas na matéria: '))

total_aulas = 40
min_presenca = total_aulas - (total_aulas * 0.75)

media_anual = (nota1 + nota2 + nota3 + nota4) / 4

if media_anual >= 7 and faltas <= min_presenca:
    print(f'\n# Aprovado com média {media_anual:.1f}'
          f'\n# Média mínima para aprovação: 7.0'
          f'\n# Frequência mínima para aprovação: 75%'
          f'\n# Número de frequência na disciplina: {(1 - (faltas/total_aulas)) * 100:.0f}%'
          f'\n# Número de faltas: {faltas}')

elif media_anual < 7 and faltas > 10:
    print('\n# REPROVADO por nota e número de faltas.'
          f'\n# Média mínima para aprovação: 7.0'
          f'\n# Média observada na disciplina: {media_anual:.1f}'
          f'\n# Frequência mínima para aprovação: 75%'
          f'\n# Frequência observada na disciplina: {(1 - (faltas / total_aulas)) * 100:.0f}%'
          f'\n# Número de faltas: {faltas}.')

elif faltas > 10:
    print('\n# REPROVADO por faltas: frequência abaixo de 75%'
          f'\n# Número de faltas na disciplina: {faltas}'
          f'\n# Frequência observada na disciplina: {(1 - (faltas/total_aulas)) * 100:.0f}%')
else:
    print('\n# REPROVADO por nota!'
          f'\n# Média mínima para aprovação: 7.0'
          f'\n# Sua média foi de {media_anual:.1f}')
