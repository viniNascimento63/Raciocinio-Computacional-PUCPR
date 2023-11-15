frutas = ['maça', 'banana', 'pera', 'abacaxi', 'morango']
for fruta in frutas:
    print(fruta)

# Função enumerate() -> Retorna o elemento e o índice dele na lista
for i, fruta in enumerate(frutas):
    print(i, fruta)

# Também é possível definir o valor inicial de 'i'
for i, fruta in enumerate(frutas, 100):
    print(i, fruta)