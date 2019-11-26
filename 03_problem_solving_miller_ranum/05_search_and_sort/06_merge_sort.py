from typing import Any, List
import time


def merge_sort(a_list: List[Any]) -> None:

    # pass on base case when length of a_list is 1
    if len(a_list) > 1:

        # slice into left and right halves
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        # merge sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # assuming left_half and right_half are sorted, merge them
        i = j = k = 0

        # go through the list, setting each element with index k appropriately
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]

                i += 1
                k += 1
            else:
                a_list[k] = right_half[j]
                j += 1
                k += 1

        if i == len(left_half):
            while j < len(right_half):
                a_list[k] = right_half[j]
                k += 1
                j += 1

        if j == len(right_half):
            while i < len(left_half):
                a_list[k] = left_half[i]
                k += 1
                i += 1

        return a_list

    else:
        return a_list


if __name__ == "__main__":
    # testing slicing

    def time_slice(n: int) -> int:
        a = list(range(n))
        half = n // 2

        start = time.time()
        b = a[:half]
        return time.time() - start

    # for i in range(5, 10):
    #     print(i)
    #     print(time_slice(10 ** i))

    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(a))
