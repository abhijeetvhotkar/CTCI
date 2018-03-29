def rotate_matrix(mat):
    length = len(mat)
    for row in range(length // 2):
        for col in range(row, length - 1 - row):
            mat[col][length - row - 1], mat[length - row - 1][length - col - 1], mat[length - col - 1][row], mat[row][col] = \
            mat[row][col], mat[col][length - row - 1], mat[length - row - 1][length - col - 1], mat[length - col - 1][row]
    return print(mat)

mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

rotate_matrix(mat)
