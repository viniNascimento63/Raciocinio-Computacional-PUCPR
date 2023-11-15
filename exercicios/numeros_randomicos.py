from math import sqrt
import random
import string

print(f'\n# A raiz quadrade de 25 = {sqrt(25):.0f}')
print(f'# Número aleatório de 1 a 100: {random.randint(1, 100)}')
print(f'# Número aleatório a partir de -10 a 10: {random.randrange(-10, 10, 2)}')
# random.randrange(10): vai de 0 a 9
print(f'# Número real aleatório: {random.random()}')
print(f'# Número real dentro de uma faixa de valores: {random.uniform(-5, 5)}')
print(f"# Selecionando caractere aleatório da palavra ABACAXI: {random.choice('ABACAXI')}")
print(f'# Selecionando um caractere aleatório do alfabeto: {random.choice(string.ascii_uppercase)}')
