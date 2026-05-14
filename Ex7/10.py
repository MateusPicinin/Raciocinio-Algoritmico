import random

print('\n\n\n\n\n\n\n\n')

tabuleiro1 = [' ', ' ', ' ']
tabuleiro2 = [' ', ' ', ' ']
tabuleiro3 = [' ', ' ', ' ']

jogador = 'X'
maquina = 'O'

print('Vamos jogar jogo da velha, escolha uma posição de 0 a 8\n')

print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)

primeira = int(input('Digite aqui a posição: '))

if primeira < 3:
    tabuleiro1[primeira] = jogador

elif primeira < 6:
    tabuleiro2[primeira - 3] = jogador

elif primeira < 9:
    tabuleiro3[primeira - 6] = jogador

else:
    print('Posição inválida!')

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)





print('\nTurno da máquina:')

segunda = random.randint(0, 8)

while segunda == primeira:
    segunda = random.randint(0, 8)

if segunda < 3:
    tabuleiro1[segunda] = maquina

elif segunda < 6:
    tabuleiro2[segunda - 3] = maquina

elif segunda < 9:
    tabuleiro3[segunda - 6] = maquina


print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)





print('Sua vez')

terceira = int(input('Digite aqui a posição: '))
while terceira == segunda or terceira == primeira:
    print('Essa posição ja foi escolhida!! ')
    terceira = int(input('Digite aqui a posição: '))

if terceira < 3:
    tabuleiro1[terceira] = jogador

elif terceira < 6:
    tabuleiro2[terceira - 3] = jogador

elif terceira < 9:
    tabuleiro3[terceira - 6] = jogador

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)











print('\nTurno da máquina:')

quarta = random.randint(0, 8)

while quarta == terceira or quarta == segunda or quarta == primeira:
    quarta = random.randint(0, 8)

if quarta < 3:
    tabuleiro1[quarta] = maquina

elif quarta < 6:
    tabuleiro2[quarta - 3] = maquina

elif quarta < 9:
    tabuleiro3[quarta - 6] = maquina

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)









print('Sua vez')

quinta = int(input('Digite aqui a posição: '))
while quinta == quarta or quinta == terceira or quinta == segunda or quarta == primeira:
    print('Essa posição ja foi escolhida!! ')
    terceira = int(input('Digite aqui a posição: '))

if quinta < 3:
    tabuleiro1[quinta] = jogador

elif quinta < 6:
    tabuleiro2[quinta - 3] = jogador

elif quinta < 9:
    tabuleiro3[quinta - 6] = jogador

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)






print('\nTurno da máquina:')

sexta = random.randint(0, 8)

while sexta == quinta or sexta == quarta or sexta == terceira or sexta == segunda or sexta == primeira:
    sexta = random.randint(0, 8)

if sexta < 3:
    tabuleiro1[sexta] = maquina

elif sexta < 6:
    tabuleiro2[sexta - 3] = maquina

elif sexta < 9:
    tabuleiro3[sexta - 6] = maquina

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)







print('Sua vez')

setima = int(input('Digite aqui a posição: '))
while setima == sexta or setima == quinta or setima == quarta or setima == terceira or setima == segunda or setima == primeira:
    print('Essa posição ja foi escolhida!! ')
    setima = int(input('Digite aqui a posição: '))

if setima < 3:
    tabuleiro1[setima] = jogador

elif setima < 6:
    tabuleiro2[setima - 3] = jogador

elif setima < 9:
    tabuleiro3[setima - 6] = jogador

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)









print('\nTurno da máquina:')

oitava = random.randint(0, 8)

while oitava == setima or oitava == sexta or oitava == quinta or oitava == quarta or oitava == terceira or oitava == segunda or oitava == primeira:
    oitava = random.randint(0, 8)

if oitava < 3:
    tabuleiro1[oitava] = maquina

elif oitava < 6:
    tabuleiro2[oitava - 3] = maquina

elif oitava < 9:
    tabuleiro3[oitava - 6] = maquina

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)










print('Sua vez')

nona = int(input('Digite aqui a posição: '))
while nona == oitava or nona == setima or nona == sexta or nona == quinta or nona == quarta or nona == terceira or nona == segunda or nona == primeira:
    print('Essa posição ja foi escolhida!! ')
    nona = int(input('Digite aqui a posição: '))

if nona < 3:
    tabuleiro1[nona] = jogador

elif nona < 6:
    tabuleiro2[nona - 3] = jogador

elif nona < 9:
    tabuleiro3[nona - 6] = jogador

print()
print(tabuleiro1)
print(tabuleiro2)
print(tabuleiro3)







print('\n\n\n\n')



if tabuleiro1[0] == 'X' and tabuleiro1[1] == 'X' and tabuleiro1[2] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro2[0] == 'X' and tabuleiro2[1] == 'X' and tabuleiro2[2] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro3[0] == 'X' and tabuleiro3[1] == 'X' and tabuleiro3[2] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro1[0] == 'X' and tabuleiro2[0] == 'X' and tabuleiro3[0] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro1[1] == 'X' and tabuleiro2[1] == 'X' and tabuleiro3[1] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro1[2] == 'X' and tabuleiro2[2] == 'X' and tabuleiro3[2] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro1[0] == 'X' and tabuleiro2[1] == 'X' and tabuleiro3[2] == 'X':
    print('O jogador venceu!!!')
elif tabuleiro1[2] == 'X' and tabuleiro2[1] == 'X' and tabuleiro3[0] == 'X':
    print('O jogador venceu!!!')


elif tabuleiro1[0] == 'O' and tabuleiro1[1] == 'O' and tabuleiro1[2] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro2[0] == 'O' and tabuleiro2[1] == 'O' and tabuleiro2[2] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro3[0] == 'O' and tabuleiro3[1] == 'O' and tabuleiro3[2] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro1[0] == 'O' and tabuleiro2[0] == 'O' and tabuleiro3[0] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro1[1] == 'O' and tabuleiro2[1] == 'O' and tabuleiro3[1] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro1[2] == 'O' and tabuleiro2[2] == 'O' and tabuleiro3[2] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro1[0] == 'O' and tabuleiro2[1] == 'O' and tabuleiro3[2] == 'O':
    print('O máquina venceu!!!')
elif tabuleiro1[2] == 'O' and tabuleiro2[1] == 'O' and tabuleiro3[0] == 'O':
    print('A máquina venceu!!!') 

else:
    print('O jogo empatou!!!')