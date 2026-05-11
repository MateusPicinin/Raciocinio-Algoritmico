A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pares = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
contador = 0
for i in range(0, 10):
    a = int(input('Digite 10 numeros: '))
    A[i] = a
    if a%2 == 0:
        contador += 1
        pares[i] = a

print(f'Os numeros escolhidos foram: {A}\n')
print(f'O total de numeros pares foram: {contador}\n')
print(f'Os numeros pares são: {pares}\n Ignore os 0')