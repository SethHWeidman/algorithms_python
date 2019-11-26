class BinaryTree(object):
    def __init__(self, val: int):
        self.key = val
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, val: int) -> None:
        """
        Note: accepts an integer as a value (not a tree), and inserts value as the left child of the root.
        """
        if not self.left_child:
            self.left_child = BinaryTree(val)
        else:
            new_tree = BinaryTree(val)
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right_child(self, val: int) -> None:
        """
        Note: accepts an integer as a value (not a tree), and inserts value as the right child of the root.
        """
        if not self.right_child:
            self.right_child = BinaryTree(val)
        else:
            new_tree = BinaryTree(val)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def get_left_child(self) -> "BinaryTree":
        return self.left_child

    def get_right_child(self) -> "BinaryTree":
        return self.right_child

    def set_root_val(self, val: int) -> None:
        self.key = val

    def get_root_val(self) -> int:
        return self.key


if __name__ == "__main__":
    r = BinaryTree(1)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left_child(2)
    print(r.get_root_val())
    print(r.get_left_child().get_root_val())
    r.insert_right_child(3)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(4)
    print(r.get_right_child().get_root_val())
