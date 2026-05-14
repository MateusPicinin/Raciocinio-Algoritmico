A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = []
for i in range(0, 10):
    B.append(A[i]**2)

print(B)
print(f'A soma total da lista foi: {sum(B)}')