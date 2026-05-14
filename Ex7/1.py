import random

A = []

for i in range(0, 5):
    i = random.randint(1, 100)
    A.append(i)
print(f'Sua lista com 5 numeros aleatorios: {A}')