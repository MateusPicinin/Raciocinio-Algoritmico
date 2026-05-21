def soma(x, y):
    return (x+y)

def subtração(X, Y):
    return X-Y

def multiplicação(X, Y):
    return X*Y

def divisão(X, Y):
    return X/Y

Ativo = True

while Ativo:
    print('\n=-=-=-=-=-=-=-=-=-=-=-=\n')
    print('Escolha uma opação')
    print('Soma          | 1')
    print('Subtração     | 2')
    print('Multiplicação | 3')
    print('Divisão       | 4  \n')
    print('=-=-=-=-=-=-=-=-=-=-=-=\n')

    A = int(input('Digite sua opção: '))
    if A > 0 and A < 5:
        Ativo = False
    else:
        print('Escolha invalida!! ')
print('Sabendo que os valores serão calculados na ordem digitada.\n')
Valor1 = float(input('Digite o primeiro valor: '))
Valor2 = float(input('\nAgora o segundo: '))

if A == 1:
    print(f'O valor da soma foi: {soma(Valor1, Valor2)}')
elif A == 2:
    print(f'O valor da subtração foi: {subtração(Valor1, Valor2)}')
elif A == 3:
    print(f'O valor da multiplicação foi: {multiplicação(Valor1, Valor2)}')
elif A == 4:
    print(f'O valor da divisão foi: {divisão(Valor1, Valor2)}')
