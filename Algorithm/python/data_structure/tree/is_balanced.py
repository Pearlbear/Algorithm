from unittest import TestCase
from .BinaryTree import BinaryTree


class TestIsBalanced(TestCase):
    def test_is_balanced(self):
        self.assertTrue(is_balanced(BinaryTree(1, BinaryTree(2, BinaryTree(4), BinaryTree(5, BinaryTree(7))),
                                                BinaryTree(3, None, BinaryTree(6)))))
        self.assertFalse(is_balanced(BinaryTree(1, BinaryTree(2, BinaryTree(4), BinaryTree(5, BinaryTree(7, BinaryTree(8)))),
                                                BinaryTree(3, None, BinaryTree(6)))))
        self.assertTrue(is_balanced(BinaryTree(1)))
        self.assertTrue(is_balanced(BinaryTree(1, BinaryTree(2))))
        self.assertFalse(is_balanced(BinaryTree(1, BinaryTree(2, BinaryTree(3)))))
        self.assertTrue(is_balanced(BinaryTree(10, BinaryTree(6, BinaryTree(4), BinaryTree(8)),
                                               BinaryTree(14, BinaryTree(12), BinaryTree(16)))))
        self.assertTrue(is_balanced(BinaryTree(10, BinaryTree(6, BinaryTree(4), BinaryTree(8)), BinaryTree(14))))


def is_balanced(tree):
    def driver(current_node):
        if not current_node:
            return True, 0
        left_balance, left_depth = driver(current_node.left)
        right_balance, right_depth = driver(current_node.right)
        return left_balance and right_balance and (abs(left_depth - right_depth) <= 1), max(left_depth, right_depth) + 1

    balance, _ = driver(tree)
    return balance
