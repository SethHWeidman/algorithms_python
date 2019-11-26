from typing import Any, List


def partition(a_list: List[Any], start, end) -> None:

    pivot = a_list[start]

    left_index = start + 1
    right_index = end

    done = False

    while not done:
        # Need second condition: otherwise, left_index may never be less than pivot, and it will just keep incrementing
        while a_list[left_index] <= pivot and right_index >= left_index:
            left_index += 1

        while a_list[right_index] >= pivot and right_index >= left_index:

            right_index -= 1

        if right_index <= left_index:
            done = True
        else:
            a_list[left_index], a_list[right_index] = (
                a_list[right_index],
                a_list[left_index],
            )

    a_list[start], a_list[right_index] = a_list[right_index], a_list[start]

    return right_index


def quick_sort_helper(a_list: List[Any], start: int, end: int) -> None:

    if start < end:

        split_element = partition(a_list, start, end)

        partition(a_list, start, split_element)
        partition(a_list, split_element + 1, end)

        return a_list[start:end]

    else:
        return [a_list[start]]


def quick_sort(a_list: List[Any]) -> None:

    return quick_sort_helper(a_list, 0, len(a_list) - 1)


if __name__ == "__main__":

    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(a))

    b = [2]
    print(quick_sort(b))
