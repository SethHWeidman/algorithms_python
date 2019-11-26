from typing import List, Union

Tree = List[Union[int, List]]


def make_tree(r: int) -> Tree:
    return [r, [], []]


def insert_left_child(root: Tree, new_tree: Union[int, List]) -> Tree:

    current_left = root.pop(1)

    # if there is already a left tree
    if len(current_left) > 0:
        root.insert(1, [new_tree, current_left, []])
    else:
        root.insert(1, [new_tree, [], []])

    return root


def insert_right_child(root: Tree, new_tree: Union[int, List]) -> List:

    current_right = root.pop(2)

    # if there is already a right tree
    if len(current_right) > 0:
        root.insert(2, [new_tree, [], current_right])
    else:
        root.insert(2, [new_tree, [], []])

    return root


def get_root_val(tree: Tree) -> int:
    return tree[0]


def set_root_val(tree: Tree, val: int) -> Tree:

    tree[0] = val

    return tree


def get_left_child(tree: Tree) -> Tree:

    return tree[1]


def get_right_child(tree: Tree) -> Tree:

    return tree[2]


if __name__ == "__main__":
    r = make_tree(3)
    insert_left_child(r, 4)
    insert_left_child(r, 5)
    insert_right_child(r, 6)
    insert_right_child(r, 7)
    l = get_left_child(r)
    print(l)

    set_root_val(l, 9)
    print(r)
    insert_left_child(l, 11)
    print(r)
    print(get_right_child(get_right_child(r)))
