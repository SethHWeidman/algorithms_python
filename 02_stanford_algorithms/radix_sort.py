'''
https://brilliant.org/wiki/radix-sort/
'''

import math
import random
import typing


def counting_sort_digit(A: typing.List[int], digit: int, radix: int):
    B = [0] * len(A)
    C = [0] * radix
    for el in A:
        digit_of_el = int(math.floor(el / (radix ** digit))) % radix
        C[digit_of_el] += 1
    for i in range(1, radix):
        C[i] = C[i] + C[i - 1]
    for el in reversed(A):
        digit_of_el = int(math.floor(el / (radix ** digit))) % radix
        B[C[digit_of_el] - 1] = el
        C[digit_of_el] -= 1
    return B


def radix_sort(L: typing.List, radix: int):
    for i in range(radix):
        L = counting_sort_digit(L, i, radix)
    return L


if __name__ == '__main__':
    alist = random.choices(list(range(0, 999)), k=100)
    print("Unsorted list")
    print(alist)
    print()
    print("Sorted list")
    print(radix_sort(alist, 10))
