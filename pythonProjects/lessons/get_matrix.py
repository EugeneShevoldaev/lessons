def get_matrix(n, m, value):
    mtr = []
    for i in range(n):
        row = []
        for j in range(m):
             row.append(value)
        mtr.append(row)
    return mtr

mt = get_matrix(3, 5, 7)
print(mt)
