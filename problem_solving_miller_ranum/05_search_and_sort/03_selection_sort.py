from typing import Any, List


def selection_sort(a_list: List[Any]) -> None:

    for fill_slot in range(len(a_list) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[position_of_max]:
                position_of_max = location
        # now the position of the maximum value has been determined,
        # swap it with "fill_slot"
        a_list[fill_slot], a_list[position_of_max] = (
            a_list[position_of_max],
            a_list[fill_slot],
        )


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(a_list)
    print(a_list)
