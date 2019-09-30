
from data_structures import Node, UnorderedList


def delete_duplicates(u: UnorderedList) -> None:
    '''
    Runs in O(N) time
    '''
    d = {}
    previous = Node()
    node = u.head
    while node is not None:
        if node.get_data() in d:  # will never happen for the first Node
            previous.set_next(node.get_next())
        else:
            d[node.get_data()] = True
            previous = node
        node = node.get_next()


def delete_duplicates_no_buffer(u: UnorderedList) -> None:
    '''
    Runs in O(N^2) time, but O(1) space
    '''
    current = u.head
    while current is not None:
        runner = current
        while runner.get_next() is not None:
            if runner.get_next().get_data() == current.get_data():
                runner.set_next(runner.get_next().get_next())
            else:
                runner = runner.get_next()
        current = current.get_next()


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
    delete_duplicates_no_buffer(u)
    print(u)