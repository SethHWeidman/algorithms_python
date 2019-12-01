class BinarySearchTree(object):
    def __init__(self):

        self.root = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def __len__(self) -> int:
        return self.length()

    def get(self, key: str) -> int:
        val = None
        if self.root:
            val = self._get(key, self.root)
        return val

    def _get(self, key: str, current_node: "TreeNode") -> int:
        if key == current_node.key:
            return current_node.payload
        elif key < current_node.key:
            if not current_node.has_left_child():
                return None
            else:
                return self._get(key, current_node.left_child)
        else:
            if not current_node.has_right_child():
                return None
            else:
                return self._get(key, current_node.right_child)

    def put(self, key: str, val: int) -> None:
        if self.root:
            self._put(key, val, self.root)
            self.size += 1
        else:
            self.root = TreeNode(key, val)

    def _put(self, key: str, val: int, current_node: "TreeNode") -> None:
        if key == current_node.key:
            current_node.payload = val
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def delete(self, key: str) -> None:
        node_to_delete = self.get(key)

        if node_to_delete:
            node_to_delete.remove()
            self.size -= 1

    def __getitem__(self, key: str) -> int:
        return self.get(key)

    def __setitem__(self, key: str, val: int) -> None:
        self.put(key, val)

    def __delitem__(self, key: str) -> None:
        self.delete(key)

    def __iter__(self):
        pass


class TreeNode(object):
    def __init__(
        self,
        key: str,
        val: int,
        left_child: "TreeNode" = None,
        right_child: "TreeNode" = None,
        parent: "TreeNode" = None,
    ):

        self.key = key
        self.payload = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def has_left_child(self) -> bool:
        return True if self.left_child is not None else False

    def has_right_child(self) -> bool:
        return True if self.right_child is not None else False

    def is_root(self) -> bool:
        return self.parent is None

    def is_parent(self) -> bool:
        return self.has_left_child() or self.has_right_child()

    def is_left_child(self) -> bool:
        return self.parent is not None and self.parent.left_child == self

    def is_right_child(self) -> bool:
        return self.parent is not None and self.parent.right_child == self

    def has_both_children(self) -> bool:
        return self.has_left_child() and self.has_right_child()

    def is_leaf(self) -> bool:
        return not self.has_left_child() and not self.has_right_child()

    def splice_out(self) -> None:
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:
            if self.is_left_child():
                if self.has_left_child():
                    # arbitrarily check first to put the left child in the parent's place
                    self.parent.left_child = self.left_child
                else:
                    self.parent.left_child = self.right_child
            else:
                if self.has_left_child():
                    self.parent.right_child = self.left_child
                else:
                    self.parent.right_child = self.right_child

    def find_min(self) -> "TreeNode":
        current_node = self
        while current_node:
            current_node = current_node.left_child
        return current_node

    def find_successor(self) -> "TreeNode":
        if self.has_right_child():
            return self.right_child.find_min()
        else:
            if self.is_left_child():
                return self.parent
            else:
                self.parent.right_child = None
                self.parent.find_successor()
                self.parent.right_child = self

    def replace_node_data(
        self, key: str, val: int, left_child: "TreeNode", right_child: "TreeNode"
    ) -> None:
        self.key = key
        self.payload = val
        self.left_child = left_child
        self.right_child = right_child

    def remove(self, key: str) -> None:
        # only called if self is not root
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_both_children():
            successor = self.find_successor()
            successor.splice_out()
            self.key = successor.key
            self.payload = successor.payload
        else:
            # four cases when node has just one child
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                    self.left_child.parent = self.parent
                elif self.is_right_child():
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
                else:
                    self.replace_node_data(
                        self.left_child.key,
                        self.left_child.payload,
                        left_child=self.left_child.left_child,
                        right_child=self.left_child.right_child,
                    )
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                    self.right_child.parent = self.parent
                elif self.is_right_child():
                    self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent
                else:
                    self.replace_node_data(
                        self.right_child.key,
                        self.right_child.payload,
                        left_child=self.right_child.left_child,
                        right_child=self.right_child.right_child,
                    )


if __name__=='__main__':

    my_tree = BinarySearchTree()
    my_tree['a'] = 1
    my_tree['b'] = 2
    my_tree['c'] = 3
    my_tree['d'] = 4

    print(my_tree['b'])
    print(my_tree['c'])    