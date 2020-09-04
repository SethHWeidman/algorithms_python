import s3_helpers


def between(a, b, c):
    """
    Determines if an element is between two other elements
    param a: The number that may be between b and c
    param b: A potential lower/upper bound
    param c: A potential upper/lower bound
    return: True if a is between b and c, False otherwise
    """
    return (a <= b and a >= c) or (a >= b and a <= c)


def find_middle(input_list):
    """
    Finds the middle element of a list of length 3
    param input_list: a list of length 3
    return: (the index of the element to return, the element)
    """
    assert len(input_list) == 3

    a = input_list[0]
    b = input_list[1]
    c = input_list[2]
    if between(a, b, c):
        return 0
    elif between(b, a, c):
        return 1
    else:
        return 2


def select_median(input_list):
    """
    Chooses the first, middle, and last elements of the list.
    Returns the index and element value of the middle of these three elements.
    param input_list: a list of length > 1
    return: index of element, element itself
    """

    assert len(input_list) > 1

    if len(input_list) < 3:
        i = 1
    else:
        mid = (len(input_list) + 1) // 2 - 1
        end = len(input_list) - 1

        a = input_list[0]
        b = input_list[mid]
        c = input_list[end]
        index = find_middle([a, b, c])

        # Set "i"
        if index == 0:
            i = 0
        elif index == 1:
            i = mid
        elif index == 2:
            i = end

    return i, input_list[i]


class QuickSort:
    """
    Implements the Quick Sort algorithm and counts the number of comparisons done during the algorithm.
    """

    def __init__(self):
        """
        Initialize the number of comparisons done to 0.
        """
        self.comparisons = 0

    def sort_pivot_first(self, input_list):
        """
        Implements the Quick Sort algorithm choosing the first element as the pivot
        param input_list: the list to be sorted
        return: the sorted list
        """

        # Base case
        if len(input_list) == 1 or len(input_list) == 0:
            return input_list

        pivot = input_list[0]

        # Any time we sort a list of n elements, we must do n-1 comparisons:
        # Comparing the pivot element to every other element in the list
        self.comparisons += len(input_list) - 1

        left_list, right_list = self.partition_linear(input_list, pivot)

        # Recursive call
        return self.sort_pivot_first(left_list) + [pivot] + self.sort_pivot_first(right_list)

    def sort_pivot_last(self, input_list):
        """
        Implements the Quick Sort algorithm choosing the *last* element as the pivot
        param input_list: the list to be sorted
        return: the sorted list
        """

        if len(input_list) == 1 or len(input_list) == 0:
            return input_list

        pivot = input_list[-1]

        input_list[-1], input_list[0] = input_list[0], input_list[-1]

        self.comparisons += len(input_list) - 1

        left_list, right_list = self.partition_linear(input_list, pivot)

        return self.sort_pivot_last(left_list) + [pivot] + self.sort_pivot_last(right_list)

    def sort_pivot_median(self, input_list):

        if len(input_list) == 1 or len(input_list) == 0:
            return input_list

        # Use helper functions to select "median"
        index, pivot = select_median(input_list)

        input_list[index], input_list[0] = input_list[0], input_list[index]

        self.comparisons += len(input_list) - 1

        left_list, right_list = self.partition_linear(input_list, pivot)

        return self.sort_pivot_median(left_list) + [pivot] + self.sort_pivot_median(right_list)

    def partition_linear(self, input_list, pivot):
        """
        Key method: partitions a list around a pivot.
        The pivot is the first element (index 0), which is why we start with i=1 (instead of 0).
        Overview:
        1) loop through the input list.
        2) If we find an element less than the pivot, swap the elements,
        and then increment i, the location that we are "swapping to".
        param input_list: the list to be partitioned
        param pivot: the pivot element
        return: the left and right lists, where every element in the left list
        is less than every element in the right list
        """
        i = 1

        for j in range(1, len(input_list)):
            # "Do nothing" case
            if input_list[j] > pivot:
                continue
            else:
                # Swap
                input_list[i], input_list[j] = input_list[j], input_list[i]
                i += 1

        # Finally, swap the pivot with the appropriate element
        input_list[0], input_list[i - 1] = input_list[i - 1], input_list[0]

        # And return the two sublists, excluding the pivot
        return input_list[: i - 1], input_list[i:]


if __name__ == "__main__":

    stanford_bucket = s3_helpers.get_s3_bucket("stanford-algorithms")

    input_list = s3_helpers.get_object_from_bucket(stanford_bucket, "median-maintenance")

    q1 = QuickSort()
    q1.sort_pivot_first(input_list)
    assert q1.comparisons == 153929

    q2 = QuickSort()
    q2.sort_pivot_last(input_list)
    assert q2.comparisons == 203320

    q3 = QuickSort()
    q3.sort_pivot_median(input_list)
    assert q3.comparisons == 135790

