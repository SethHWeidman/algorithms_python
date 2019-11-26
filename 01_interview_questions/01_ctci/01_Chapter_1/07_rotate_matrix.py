from typing import List

Matrix = List[List[int]]


def rotate_matrix(m: Matrix) -> Matrix:
    """
    Assumes that the matrix is square - same number of rows as columns
    O(N^2) time
    """
    print(m)
    n = len(m)

    if n != len(m[0]) or n == 0:
        raise ValueError
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first

            # save top
            top = m[first][i]

            # left -> top
            m[first][i] = m[last - offset][first]

            # bottom -> left
            m[last - offset][first] = m[last][last - offset]

            # right -> bottom
            m[last][last - offset] = m[i][last]

            # top -> right
            m[i][last] = top

    print(m)


if __name__ == "__main__":
    print(rotate_matrix([[2, 3, 4], [1, 2, 0], [3, 4, 5]]))
