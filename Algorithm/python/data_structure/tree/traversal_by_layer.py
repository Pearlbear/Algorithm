from unittest import TestCase
from .BinaryTree import BinaryTree
from ..queue.Queue import Queue


class TestTraversal(TestCase):
    def test_traversal(self):
        tree = BinaryTree(1, BinaryTree(2, BinaryTree(4), BinaryTree(5)),
                          BinaryTree(3, BinaryTree(6), BinaryTree(7)))
        tree_list = traversal_by_layer(tree)
        self.assertEqual(len(tree_list), 7)
        for i in range(0, len(tree_list) - 1):
            self.assertLess(tree_list[i], tree_list[i + 1])


def traversal_by_layer(tree):
    queue = Queue()
    result = []
    if tree:
        queue.enqueue(tree)
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.key)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return result
