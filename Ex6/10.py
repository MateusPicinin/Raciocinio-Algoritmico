A = [0, 0, 0, 0, 0]
soma = 0
for i in range(0, 5):
    a = float(input('Digite 5 numeros: '))
    A[i] = a
    soma += a
    divisao = soma/5

print(max(A))
print(min(A))
print(f'A media é: {divisao}')