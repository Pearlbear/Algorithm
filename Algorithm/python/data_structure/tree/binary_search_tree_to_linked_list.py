from unittest import TestCase
from .BinaryTree import BinaryTree


class TestConvert(TestCase):
    def test_binary_search_tree_to_linked_list(self):
        tree = BinaryTree(10, BinaryTree(6, BinaryTree(4), BinaryTree(8)), BinaryTree(14, BinaryTree(12), BinaryTree(16)))
        linked_list = binary_search_tree_to_linked_list(tree)
        self.assertEqual(linked_list.key, 4)
        self.assertEqual(linked_list.left, None)
        self.assertEqual(linked_list.right.key, 6)
        self.assertEqual(linked_list.right.left.key, 4)
        self.assertEqual(linked_list.right.right.key, 8)
        self.assertEqual(linked_list.right.right.left.key, 6)
        self.assertEqual(linked_list.right.right.right.key, 10)
        self.assertEqual(linked_list.right.right.right.left.key, 8)
        self.assertEqual(linked_list.right.right.right.right.key, 12)
        self.assertEqual(linked_list.right.right.right.right.left.key, 10)
        self.assertEqual(linked_list.right.right.right.right.right.key, 14)
        self.assertEqual(linked_list.right.right.right.right.right.left.key, 12)
        self.assertEqual(linked_list.right.right.right.right.right.right.key, 16)
        self.assertEqual(linked_list.right.right.right.right.right.right.left.key, 14)
        self.assertEqual(linked_list.right.right.right.right.right.right.right, None)


def binary_search_tree_to_linked_list(tree):
    def convert(root_of_tree):
        if not root_of_tree:
            return None, None
        first_node, last_node = root_of_tree, root_of_tree
        if root_of_tree.left:
            first_node, last_node_of_left = convert(root_of_tree.left)
            last_node.left = last_node_of_left
            last_node_of_left.right = last_node
        if root_of_tree.right:
            first_node_of_right, last_node_of_right = convert(root_of_tree.right)
            last_node.right = first_node_of_right
            first_node_of_right.left = last_node
            last_node = last_node_of_right
        return first_node, last_node

    first, _ = convert(tree)
    return first

