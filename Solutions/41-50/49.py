# Program to multiply two matrices using nested loops

# take a 3x3 matrix
matrix_a = [[12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]]

# take a 3x4 matrix
matrix_b = [[5, 8, 1, 2],
            [6, 7, 3, 0],
            [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


def multiply_matrix(A, B):
    for i in range(len(A)):

        # iterating by coloum by B
        for j in range(len(B[0])):

            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    print(result);

multiply_matrix(matrix_a, matrix_b)
