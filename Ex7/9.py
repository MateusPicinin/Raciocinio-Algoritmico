import random

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

random.shuffle(A)
print('Tente advinhar uma letra do alfabeto embaralhado e sua respectiva posição: ')
Posicao = int(input('posição: '))
Letra = input('Letra: ').lower()

if A[Posicao] == Letra:
    print('\n PARABENS!!, voce acertou')
else:
    print('Voce errou :( ')

print('\n', A)