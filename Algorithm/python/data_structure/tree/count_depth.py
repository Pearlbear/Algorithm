from unittest import TestCase
from .BinaryTree import BinaryTree


class TestCountDepth(TestCase):
    def test_count_depth(self):
        tree = BinaryTree(1, BinaryTree(2, BinaryTree(4), BinaryTree(5, BinaryTree(7))),
                          BinaryTree(3, None, BinaryTree(6)))
        self.assertEqual(test_count_depth(tree), 4)
        self.assertEqual(test_count_depth(BinaryTree(1)), 1)
        self.assertEqual(test_count_depth(None), 0)


def test_count_depth(tree):
    if not tree:
        return 0
    return 1 + max(test_count_depth(tree.left), test_count_depth(tree.right))
