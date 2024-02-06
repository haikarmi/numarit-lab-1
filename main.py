def init_matrix(matrix, size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append(float(input("Enter the item " + str(i + 1) + ":" + str(j + 1) + ": ")))
        matrix.append(row)
    return matrix
# def sum_matrix(matrix):




size = int(input("Enter the matrix size\n"))
matrix = []
matrix_2 = []
matrix = init_matrix(matrix, size)
for i in range(size):
    print(matrix[i])
print(" enter the matrix num 2")
matrix_2 = init_matrix(matrix_2, size)
for i in range(size):
    print(matrix_2[i])
