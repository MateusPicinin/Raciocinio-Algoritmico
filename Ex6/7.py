A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    a = int(input('Digite 10 valores: '))
    A[i] = a


maior = A[0]
posicao = 0

for i in range(1, 10):
    if A[i] > maior:
        maior = A[i]
        posicao = i

print(A)
print(f'O maior numero foi: {max(A)}')
print(f'O indice do maior numero é: {posicao}')
