from typing import List


def list_sum(num_list: List[int]) -> int:
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


if __name__ == "__main__":
    print(list_sum([1, 2, 3, 4, 5]))
