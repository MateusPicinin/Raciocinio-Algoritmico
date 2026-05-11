A = [0, 0, 0, 0, 0, 0, 0, 0,]
soma = 0
for i in range(0, 8):
    a = int(input('Digite 8 valores: '))
    A[i] = a
print(A)

for i in range(0, 2):
    indice = int(input('Escolha o indice da casa que deseja alterar: '))
    numero = int(input('Digite o número que voce quer colocar nessa casa: '))
    if indice < 2 or indice > 7:
        print('Indice invalido!!!')
    soma += numero
    A[indice] = numero
print(f'Seu vetor ficou com os seguintes valores: {A}')
print(f'A soma dos valores alterados foi: {soma}')

