import algorithms_python.problem_solving_miller_ranum.data_structures as ds
import operator


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


operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def evaluate_parse_tree(tree: ds.BinaryTree) -> int:

    left_child = tree.get_left_child()
    right_child = tree.get_right_child()

    root_op = tree.get_root_val()

    if left_child and right_child:
        op = operator_dict[root_op]
        return op(evaluate_parse_tree(left_child), evaluate_parse_tree(right_child))

    else:
        return root_op


def evaluate_expression(expr: str) -> int:
    tree = create_parse_tree(expr)
    return evaluate_parse_tree(tree)


if __name__ == "__main__":
    print(evaluate_expression("( 3 + ( 4 * 5 ) )"))
