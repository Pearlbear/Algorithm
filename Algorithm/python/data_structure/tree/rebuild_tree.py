from unittest import TestCase
from .BinaryTree import BinaryTree


class TestRebuildTree(TestCase):
    def test_rebuild_tree(self):
        preorder = (1, 2, 4, 7, 3, 5, 6, 8)
        inorder = (4, 7, 2, 1, 5, 3, 8, 6)
        tree = rebuild_tree(preorder, inorder)
        self.assertEqual(tree.key, 1)
        self.assertEqual(tree.left.key, 2)
        self.assertEqual(tree.left.left.key, 4)
        self.assertEqual(tree.left.left.right.key, 7)
        self.assertEqual(tree.right.key, 3)
        self.assertEqual(tree.right.left.key, 5)
        self.assertEqual(tree.right.right.key, 6)
        self.assertEqual(tree.right.right.left.key, 8)


def rebuild_tree(preorder, inorder):
    if not (preorder and inorder):
        return None
    key = preorder[0]
    tree = BinaryTree(key)
    index_in_inorder = inorder.index(key)
    left_tree_inorder = inorder[:index_in_inorder]
    right_tree_inorder = inorder[index_in_inorder + 1:]
    left_tree_preorder = preorder[1:1 + len(left_tree_inorder)]
    right_tree_preorder = preorder[-len(right_tree_inorder):]
    tree.left = rebuild_tree(left_tree_preorder, left_tree_inorder)
    tree.right = rebuild_tree(right_tree_preorder, right_tree_inorder)
    return tree
