A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SomaPositivo = 0
Negativo = 0
for i in range(0, 10):
    a = float(input('Digite 10 numeros: '))
    A[i] = a
    if a > 0:
        SomaPositivo += a
    else:
        Negativo += 1

print(f' Os numeros digitados: {A}')
print(f'O total de numeris negativos foi: {Negativo}')
print(f'A soma de todos os numeros positivos: {SomaPositivo}')