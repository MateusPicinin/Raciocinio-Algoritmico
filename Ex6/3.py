A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 10):
    a = float(input('Digite um numero: '))
    A[i] = a
    B[i] = A[i]**2

print(A, '\n', B)