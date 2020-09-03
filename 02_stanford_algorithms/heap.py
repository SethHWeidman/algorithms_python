import s3_helpers


class MinHeap:
    def __init__(self):
        # Initialize array, starting from zero
        self.array = [0]
        self.size = 0

    def get_root(self):
        # Return the first element
        return self.array[1]

    def insert(self, el: int) -> None:
        # Insert element at the end, and then "bubble it up" appropriately
        self.array.append(el)
        self.size += 1

        self.bubble_up(self.size)

    def bubble_up(self, i: int) -> None:
        # Compare each element with its parent
        # The heap property requires that each parent element be less than its children
        # Thus, we compare each element with its parent, and if it is greater than it, we swap 
        # them.
        parent = i // 2

        while parent:

            if self.array[parent] > self.array[i]:  # swap!

                self.array[parent], self.array[i] = self.array[i], self.array[parent]

            i = parent
            parent = i // 2

    def extract_min(self) -> int:
        # swap min with end
        self.array[1], self.array[self.size] = self.array[self.size], self.array[1]

        min_val = self.array.pop()
        self.size -= 1

        self.bubble_down(1)

        return min_val

    def bubble_down(self, i: int) -> None:
        # Compare each element with its minimum child
        # The heap property requires that each parent element be less than its minimum child
        # Thus, we compare each element with its minimum child, and if it is greater than it,
        # we swap them.
        while 2 * i <= self.size:
            min_child_index = self.min_child_index(i)

            if self.array[i] > self.array[min_child_index]:  # swap!

                self.array[i], self.array[min_child_index] = (
                    self.array[min_child_index],
                    self.array[i],
                )

            i = min_child_index

    def min_child_index(self, i: int) -> int:
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.array[2 * i] <= self.array[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1


class MaxHeap:
    def __init__(self):
        self.array = [0]
        self.size = 0

    def get_root(self):
        return self.array[1]

    def insert(self, el):
        # Need bubble up
        self.array.append(el)
        self.size += 1

        self.bubble_up(self.size)

    def bubble_up(self, i):
        # Compare each element with its parent
        # The heap property requires that each parent element be greater than its children
        # Thus, we compare each element with its parent, and if it is less than
        # it, we swap them.
        parent = i // 2

        while parent:
            if self.array[parent] < self.array[i]:  # swap!

                self.array[parent], self.array[i] = self.array[i], self.array[parent]

            i = parent
            parent = i // 2

    def extract_max(self):
        # swap min with end
        self.array[1], self.array[self.size] = self.array[self.size], self.array[1]

        max_val = self.array.pop()
        self.size -= 1

        self.bubble_down(1)

        return max_val

    def bubble_down(self, i):
        # Compare each element with its parent
        # The heap property requires that each element be greater than its maximum child
        # Thus, we compare each element with its maximum child, and if it is less than
        # it, we swap them.
        while 2 * i <= self.size:
            max_child_index = self.max_child_index(i)

            if self.array[i] < self.array[max_child_index]:  # swap!

                self.array[i], self.array[max_child_index] = (
                    self.array[max_child_index],
                    self.array[i],
                )

            i = max_child_index

    def max_child_index(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.array[2 * i] >= self.array[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1


class MedianMaintainer:
    
    def __init__(self):
        self.high_heap = MinHeap()
        self.low_heap = MaxHeap()
        self.size = 0
        
    def insert(self, el):
        '''
        Min_heap will have at most one more element than max heap
        '''
        self.size += 1
        if self.size < 2:
            self.low_heap.insert(el)
        else:
            low_max = self.low_heap.get_root()
            if el >= low_max:
                self.high_heap.insert(el)
            else:
                self.low_heap.insert(el)
        
        med = self.size // 2
        while self.high_heap.size < med:
            self.high_heap.insert(self.low_heap.extract_max())
        while self.low_heap.size < med:
            self.low_heap.insert(self.high_heap.extract_min())
    
    def get_median(self):
        '''
        Min_heap will have at most one more element than max heap
        '''
        if self.size % 2 == 0:
            return self.low_heap.get_root() # arbitrary
        else:
            if self.low_heap.size > self.high_heap.size:
                return self.low_heap.get_root()
            else:
                return self.high_heap.get_root()


if __name__ == "__main__":

    stanford_bucket = s3_helpers.get_s3_bucket("stanford-algorithms")

    input_list = s3_helpers.get_object_from_bucket(stanford_bucket, "median-maintenance")

    m = MedianMaintainer()
    median_sum = 0
    for el in input_list:
        m.insert(el)
        med = m.get_median()
        median_sum += med

    assert median_sum == 46831213