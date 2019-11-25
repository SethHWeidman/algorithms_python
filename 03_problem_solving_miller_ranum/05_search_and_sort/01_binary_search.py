from typing import Any, List


def binary_search(a_list: List[Any], item: Any) -> bool:
    """
    Assumes a_list is sorted.
    """
    first = 0
    last = len(a_list) - 1
    found = False

    while not found and first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


if __name__ == "__main__":
    print(binary_search([1, 2, 3], 3))
    print(binary_search([1, 2, 3], 4))
