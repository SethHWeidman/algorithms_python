import algorithms_python.problem_solving_miller_ranum.data_structures as ds
from algorithms_python.problem_solving_miller_ranum.trees.parse_tree import create_parse_tree, evaluate_parse_tree

def preorder_traversal(tree: ds.BinaryTree) -> None:

    if tree:
        print(tree.get_root_val())
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())


operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def postorder_eval(tree: ds.BinaryTree) -> int:
    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return operator_dict[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()


def inorder_print(tree: ds.BinaryTree) -> str:
    s = ""
    if tree:
        s = s + inorder_print(tree.get_left_child())
        s = s + str(tree.get_root_val())
        s = s + inorder_print(tree.get_right_child())
    return s


if __name__ == "__main__":
    tree = create_parse_tree("( 3 + ( 4 * 5 ) )")
    print(postorder_eval(tree))
    print(inorder_print(tree))
