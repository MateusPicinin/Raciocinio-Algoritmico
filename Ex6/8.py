A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Soma = 0
for i in range(0, 15):
    a = float(input('Digite suas 15 notas: '))
    A[i] = a
    Soma += a
    divisao = Soma/15
print(f'As notas digitadas: {A}')
print(f'A media foi: {divisao}')
