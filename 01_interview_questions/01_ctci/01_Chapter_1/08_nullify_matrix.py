from typing import List

Matrix = List[List[int]]


def nullify_matrix(m: Matrix) -> Matrix:
    """
    Assumes that the matrix is rectangular - same number of columns in each row
    O(N^2) complexity but O(1) space
    """

    def num_rows(m: Matrix) -> int:
        return len(m)

    def num_cols(m: Matrix) -> int:
        return len(m[0])

    def nullify_row(m: Matrix, i: int) -> Matrix:
        for j in range(num_cols(m)):
            m[i][j] = 0
        return m

    def nullify_col(m: Matrix, j: int) -> Matrix:
        for i in range(num_rows(m)):
            m[i][j] = 0
        return m

    def first_row_has_zero(m: Matrix) -> bool:
        for j in range(num_cols(m)):
            if m[0][j] == 0:
                return True
        return False

    def first_col_has_zero(m: Matrix) -> bool:
        for i in range(num_rows(m)):
            if m[i][0] == 0:
                return True
        return False

    def find_zeros(m: Matrix) -> Matrix:
        for i in range(num_rows(m)):
            for j in range(num_cols(m)):
                if m[i][j] == 0:
                    m[0][j] = 0
                    m[i][0] = 0
        return m

    first_row_zero = first_row_has_zero(m)
    first_col_zero = first_col_has_zero(m)

    m = find_zeros(m)

    for i in range(num_rows(m)):
        if m[i][0] == 0:
            m = nullify_row(m, i)

    for j in range(num_cols(m)):
        if m[0][j] == 0:
            m = nullify_col(m, j)

    if first_row_zero:
        for j in range(num_cols(m)):
            m[0][j] = 0

    if first_col_zero:
        for i in range(num_cols(m)):
            m[i][0] = 0

    # handle the last element of the list
    return m


if __name__ == "__main__":
    print(nullify_matrix([[2, 3, 4], [1, 2, 0], [3, 4, 5]]))
