'''
Goal: given a list of ints, and a target sum, find the number of ways
the symbols '+' and '-' can be inserted to generate the target sum
'''

from typing import List, Union


def target_sum(ints: List[int], target: int) -> int:
    
    class Count(object):
        def __init__(self, count: int):
            self.count = count

    c = Count(0)

    def calculate(
        ints: List[int],
        index: int,
        partial_sum: int,
        target: int) -> None:

        if index == len(ints):
            if partial_sum == target:
                c.count += 1

        else:
            calculate(ints, index + 1, partial_sum + ints[index], target)
            calculate(ints, index + 1, partial_sum - ints[index], target)

    calculate(ints, 0, 0, target)

    return c.count


def target_sum_memo(ints: List[int], 
                    target: int,
                    target_max_value: int = 1000) -> int:

    class Count(object):
        def __init__(self, count: Union[int, float]):
            self.count = count

        def __add__(self, other: 'Count'):
            self.count += other.count

        def __radd__(self, other: 'Count'):
            self.count += other.count            

    c = Count(0)

    memo = [[float("-inf")] * (target_max_value * 2 + 1)] * len(ints)

    def calculate(
        ints: List[int],
        index: int,
        partial_sum: int,
        target: int,
        memo: List[List[int]]) -> None:

        if index == len(ints):
            if partial_sum == target:
                return 1
            else:
                return 0

        else:
            if memo[index][partial_sum + 1000] != float("-inf"):
                return memo[index][partial_sum + 1000]

            add = calculate(ints, index + 1, partial_sum + ints[index], target, memo)
            subtract = calculate(ints, index + 1, partial_sum - ints[index], target, memo)    

            memo[index][partial_sum + 1000] = add + subtract
            return memo[index][partial_sum + 1000]   

    return calculate(ints, 0, 0, target, memo)

    # return c.count




if __name__ == '__main__':
    # ans = target_sum([1, 1, 1, 1, 1], 3)
    ans = target_sum_memo([1, 1, 1, 1, 1], 3)    
    print(ans)  # 5
