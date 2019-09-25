from data_structures import Node, UnorderedList

class Index:
    def __init__(self, val: int):
        self.val = val

def kth_node_from_last(n: Node,
                        k: int,
                        i: Index) -> Node:
    if n is None:
        return None
    node = kth_node_from_last(n.next, k, i)
    i.val += 1
    if i.val == k:
        return n
    return node

def remove_kth_from_last(u: UnorderedList, k: int) -> Node:
    i = Index(0)
    kth_to_last_node = kth_node_from_last(u.head, k, i)
    return u.remove(kth_to_last_node.get_data())

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
    remove_kth_from_last(u, 2)
    print(u)
