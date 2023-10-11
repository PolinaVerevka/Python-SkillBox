size = int(input("Введите размерность матрицы: "))
matrix = [[j + 1 for j in range(size)] for i in range(size)]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(size):
    for j in range(i, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
print("Транспонированная матрица:")
for row in matrix:
    print(row)
