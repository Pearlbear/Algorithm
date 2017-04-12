from .BinaryTree import BinaryTree
from unittest import TestCase


class TestMirrorOfTree(TestCase):
    def test_mirror(self):
        self.assertIsNone(mirror_of_tree(None))
        one_node_tree = BinaryTree(8)
        mirror_of_one_node_tree = mirror_of_tree(one_node_tree)
        self.assertEqual(mirror_of_one_node_tree.key, 8)
        self.assertIsNone(mirror_of_one_node_tree.left)
        self.assertIsNone(mirror_of_one_node_tree.right)
        tree = BinaryTree(8, BinaryTree(8, BinaryTree(9)), BinaryTree(7))
        mirror = mirror_of_tree(tree)
        self.assertEquals(mirror.key, 8)
        self.assertEquals(mirror.left.key, 7)
        self.assertEquals(mirror.right.key, 8)
        self.assertEquals(mirror.right.right.key, 9)
        self.assertIsNone(mirror.left.left)
        self.assertIsNone(mirror.left.right)
        self.assertIsNone(mirror.right.left)
        self.assertIsNone(mirror.right.right.left)
        self.assertIsNone(mirror.right.right.right)


def mirror_of_tree(tree):
    if not tree:
        return None
    tree.left, tree.right = mirror_of_tree(tree.right), mirror_of_tree(tree.left)
    return tree
