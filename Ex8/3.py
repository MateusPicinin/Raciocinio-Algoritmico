matriz = []
maior = 0
MatriculaFinal = 0

for i in range(4):
    matricula = int(input('Digite sua matricula: '))
    MediaP = int(input('Digite sua media das provas: '))
    MediaT = int(input('Digite sua media dos trabalhos: '))
    MediaF = MediaP+MediaT
    i = [matricula, MediaP, MediaT, MediaF]
    matriz.append(i)
    if maior < MediaF:
        maior = MediaF
        MatriculaFinal = matricula

for i in range(4):
    print(matriz[i])
print('\n')
print(f'A matricula com a maior media final foi: {MatriculaFinal}')