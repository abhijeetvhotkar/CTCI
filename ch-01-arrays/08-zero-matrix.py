def zero_matrix(mat):
    length_mat, length_fst_row = len(mat), len(mat[0])
    print(length_fst_row)

    clear_fst_row = False

    for col in range(len(length_fst_row)):
        if mat[0][col] == 0:
            clear_fst_row = True
            break

    

mat = [
    [1, 2, 3, 4, 0],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 0, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

zero_matrix(mat)
