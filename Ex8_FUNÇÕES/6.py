import random
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0, 9)

def imprime_diagonal():
    for i in range(3):
        for j in range(3):
            if i == j:
                print(matriz[i][j])
imprime_diagonal()