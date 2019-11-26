import algorithms_python.problem_solving_miller_ranum.data_structures as ds


def create_parse_tree(in_str: str) -> ds.BinaryTree:
    new_tree = ds.BinaryTree(0)
    parent_stack = ds.Stack()

    current_tree = new_tree
    parent_stack.push(new_tree)

    chars = in_str.split()

    for char in chars:
        if char == "(":
            current_tree.insert_left_child(0)
            parent_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif char in "0123456789":
            current_tree.set_root_val(int(char))
            current_tree = parent_stack.pop()
        elif char in ["+", "-", "*", "/"]:
            current_tree.set_root_val(char)
            current_tree.insert_right_child(0)
            parent_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif char == ")":
            current_tree = parent_stack.pop()
        else:
            print("Invalid character")

    return new_tree
