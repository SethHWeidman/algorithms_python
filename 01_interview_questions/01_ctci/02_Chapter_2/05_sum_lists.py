from data_structures import Node, UnorderedList


def sum_linked_lists(u1: UnorderedList,
                     u2: UnorderedList,
                     carry: int = 0) -> Node:

    '''
    Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.

    '''
    h1 = u1.head
    h2 = u2.head

    if not h1 and not h2 and carry == 0:
        return None

    result = Node(None)

    value = carry
    if h1 != None:
        value += h1.get_data()
    if h2 != None:
        value += h2.get_data()
    
    result.set_data(value % 10)

    if h1 or h2:
        if not h1:
            n1 = UnorderedList()
        else:
            u1.remove_head()
            n1 = u1

        if not h2:
            n2 = UnorderedList()
        else:
            u2.remove_head()
            n2 = u2

        rest = sum_linked_lists(
            n1, n2, 1 if value >= 10 else 0
            )
        result.set_next(rest)

    return result


if __name__ == '__main__':
    u1 = UnorderedList()
    u1.add(6)
    u1.add(1)
    u1.add(7)
    u2 = UnorderedList()
    u2.add(2)
    u2.add(9)
    u2.add(5)
    new_head = sum_linked_lists(u1, u2)
    while new_head:
        new_head = new_head.get_next()


