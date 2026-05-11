A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    a = int(input('digite 10 numeros: '))
    A[i] = a
print(f'O maior numero for: {max(A)}')
print(f'O menor numero foi: {min(A)}')