from data_structures import Node, UnorderedList

def delete_middle_node(u: UnorderedList,
                       n: Node) -> bool:

    if n is None or n.get_next() is None:
        return False  # failure

    next_node = n.get_next()
    next_node.set_data(n.get_data())  # copy data from next node to this node
    n.set_next(next_node.get_next())  # delete next node
    return True


if __name__ == '__main__':
    u = UnorderedList()
    u.add(3)
    print(u.head)
    u.add(4)
    print(u.head)
    u.add(4)
    print(u)
    u.add(5)
    print(u)
    u2 = deepcopy(u)
    u3 = deepcopy(u)
    remove_kth_from_last(u2, 2)
    remove_kth_from_last_pointers(u3, 1)
    print(u2)
    print(u3)
