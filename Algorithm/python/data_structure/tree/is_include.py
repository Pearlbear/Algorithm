from .BinaryTree import BinaryTree
from unittest import TestCase


class TestIsInclude(TestCase):
    def test_is_include(self):
        tree_a = BinaryTree(8, BinaryTree(8, BinaryTree(9),
                                          BinaryTree(2, BinaryTree(4), BinaryTree(7))),
                            BinaryTree(7))
        tree_b = BinaryTree(8, BinaryTree(9), BinaryTree(2))
        self.assertTrue(is_include(tree_a, tree_b))
        tree_c = BinaryTree(8, BinaryTree(9))
        self.assertTrue(is_include(tree_a, tree_c))
        tree_d = BinaryTree(8, None, BinaryTree(2))
        self.assertTrue(is_include(tree_a, tree_d))
        tree_e = BinaryTree(8, BinaryTree(9), BinaryTree(4))
        self.assertFalse(is_include(tree_a, tree_e))

        self.assertFalse(is_include(None, tree_b))
        self.assertTrue(is_include(tree_a, None))


def is_include(tree_a, tree_b):
    def is_tree_equal(subtree_a, subtree_b):
        if subtree_a.key == subtree_b.key:
            return (is_tree_equal(subtree_a.left, subtree_b.left) if subtree_b.left else True) and (
                is_tree_equal(subtree_a.right, subtree_b.right) if subtree_b.right else True)
        else:
            return False

    if not tree_b:
        return True
    if not tree_a:
        return False
    if is_tree_equal(tree_a, tree_b):
        return True
    return is_include(tree_a.left, tree_b) or is_include(tree_a.right, tree_b)
