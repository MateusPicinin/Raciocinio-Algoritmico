A = [0, 0, 0, 0, 0]


for i in range(0, 5):
    A[i] = int(input('Digite o 5 números: '))

maior = A[0]
indiceMax = 0
menor = A[0]
indiceMin = 0

for i in range(1, 5):
    if A[i] > maior:
        maior = A[i]
        indiceMax = i
    
    if A[i] < menor:
        menor = A[i]
        indiceMin = i

print(f'\nLista digitada: {A}')
print(f'O maior valor é {maior} na posição {indiceMax}')
print(f'O menor valor é {menor} na posição {indiceMin}')
