matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input('Digite um numero: '))


maior = matriz[0][0]
linha = 0
coluna = 0

for i in range(4):
    for j in range(4):
        if maior < matriz[i][j]:
            maior = matriz[i][j]
            linha = i
            coluna = j

for i in range(4):
    print(matriz[i])
print(f'O maior numero da matriz é: {maior}')
print(f'A localização do maior numero é linha {linha} e coluna {coluna}')