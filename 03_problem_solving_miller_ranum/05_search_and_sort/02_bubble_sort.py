from typing import Any, List


def bubble_sort(a_list: List[Any]) -> None:

    for pass_num in range(len(a_list)-1, 0, -1):

        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i+1], a_list[i] = a_list[i], a_list[i+1]


def bubble_sort_short(a_list: List[Any]) -> None:

    exchanges = True

    pass_num = len(a_list) - 1

    # ensures that exchanges will stay true only if a needed swap is detected
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                a_list[i+1], a_list[i] = a_list[i], a_list[i+1]

        pass_num -= 1

if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(a_list)
    print(a_list)

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort_short(a_list)
    print(a_list)
