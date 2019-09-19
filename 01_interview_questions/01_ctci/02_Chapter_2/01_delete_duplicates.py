
from data_structures import Node, UnorderedList


def delete_duplicates(u: UnorderedList) -> None:
    '''
    Runs in O(N) time
    '''
    d = {}
    previous = Node()
    node = u.head
    while node != None:
        if node.get_data() in d: # will never happen for the first Node
            previous.set_next(node.get_next())
        else:
            d[node.get_data()] = True
            previous = node
        node = node.get_next()


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
    u.add(3)
    print(u)        
    delete_duplicates(u)
    print(u)