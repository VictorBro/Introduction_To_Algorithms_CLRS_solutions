def matrix_multiply(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])
    if cols_a != rows_b:
        raise Exception("can't multiply matrix {}x{} to {}x{}".format(rows_a, cols_a, rows_b, cols_b))
    C = []
    for i in range(rows_a):
        row_c = []
        for j in range(cols_b):
            temp = 0
            for k in range(cols_a):
                temp += A[i][k] * B[k][j]
            row_c.append(temp)
        C.append(row_c)
    return C


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
Z = matrix_multiply(X, Y)
for row_z in Z:
    print(row_z)

# result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
# [print(row) for row in result]
