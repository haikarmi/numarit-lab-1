def init_matrix(matrix, size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append(float(input("Enter the item " + str(i + 1) + ":" + str(j + 1) + ": ")))
        matrix.append(row)
    return matrix


def sum_matrix(matrix, matrix_2):
    matrix_sum = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(matrix_2[i][j] + matrix[i][j])
        matrix_sum.append(row)
    print_matrix(matrix_sum)


def print_matrix(matrix):
    for i in range(size):
        print(matrix[i])

def multiply_matrix(matrix, matrix_2):
    matrix_mul = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix_mul.append(row)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                matrix_mul[i][j] += matrix[i][k] * matrix_2[k][j]
    print_matrix(matrix_mul)

size = int(input("Enter the matrix size\n"))
matrix = []
matrix_2 = []
matrix = init_matrix(matrix, size)
print_matrix(matrix)
print(" enter the matrix num 2")
matrix_2 = init_matrix(matrix_2, size)
print_matrix(matrix_2)
print(" the sum matrix")
sum_matrix(matrix, matrix_2)
print(" the multiply matrix")
multiply_matrix(matrix,matrix_2)
