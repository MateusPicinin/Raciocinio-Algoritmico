def contar_caracteres(string, caractere):
    contador = 0


    for i in range(len(string)):
        if string[i] == caractere:
            contador += 1

    return contador



A = input('Digite uma palavra: ')
B = input('Digite um caractere: ')

print(contar_caracteres(A, B))
