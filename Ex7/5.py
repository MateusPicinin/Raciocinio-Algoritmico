A = []

for i in range(0, 5):
    a = input('Digite 5 palavras: ')
    A.append(a)

maior = A[0]
menor = A[0]

for a in A:
    if len(a) > len(maior):
        maior = a
    if len(a) < len(menor):
        menor = a

print(f'Palavra mais longa: {maior}')
print(f'Palavra mais curta: {menor}')