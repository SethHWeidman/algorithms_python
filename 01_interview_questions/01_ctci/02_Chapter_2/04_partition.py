from data_structures import Node, UnorderedList

def partition_linked_list(u: UnorderedList,
                          x: int) -> Node:

    '''
    Passes in an unordered list.
    Returns the head of a list that has been "paritioned" around x
    Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (partition: 5)
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    '''

    before_start = None
    before_end = None
    after_start = None
    after_end = None

    node = u.head
    while node:
        next_node = node.get_next()
        node.set_next(None)
        if node.get_data() < x:
            if not before_start:
                before_start = node
                before_end = before_start
            else:
                before_end.set_next(node)
                before_end = node
        else:
            if not after_start:
                after_start = node
                after_end = after_start
            else:
                after_end.set_next(node)
                after_end = node
        node = next_node

    if not before_start:
        return after_start

    before_end.set_next(after_start)
    return before_start


if __name__ == '__main__':
    u = UnorderedList()
    u.add(3)
    u.add(5)
    u.add(8)
    u.add(5)
    u.add(10)
    u.add(2)
    u.add(1)
    print(u)
    new_head = partition_linked_list(u, 5)
    while new_head:
        print(new_head)
        new_head = new_head.get_next()

