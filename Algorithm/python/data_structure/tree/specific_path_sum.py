from unittest import TestCase
from .BinaryTree import BinaryTree


class TestSpecificPathSum(TestCase):
    def test_specific_path_sum(self):
        self.assertTrue(
            specific_path_sum(BinaryTree(10, BinaryTree(5, BinaryTree(4), BinaryTree(7)), BinaryTree(12)), 22) == [
                [10, 5, 7], [10, 12]])
        self.assertTrue(
            specific_path_sum(BinaryTree(10, BinaryTree(5, BinaryTree(4), BinaryTree(7)), BinaryTree(12)), 25) == [])
        self.assertTrue(
            specific_path_sum(BinaryTree(10, BinaryTree(5, BinaryTree(4), BinaryTree(7)), BinaryTree(12)), 15) == [])
        self.assertTrue(
            specific_path_sum(BinaryTree(10, BinaryTree(5, BinaryTree(4), BinaryTree(7)), BinaryTree(12)), 19) == [
                [10, 5, 4]])
        self.assertTrue(
            specific_path_sum(None, 19) == [])


def specific_path_sum(tree, path_sum):
    result = []

    def driver(current_tree, current_path_sum, previous_path):
        if not current_tree or current_tree.key > current_path_sum:
            return
        if (current_tree.key == current_path_sum) and (not (current_tree.left or current_tree.right)):
            result.append(previous_path + [current_tree.key])
            return
        next_path_sum = current_path_sum - current_tree.key
        next_path = previous_path + [current_tree.key]
        if current_tree.left:
            driver(current_tree.left, next_path_sum, next_path[:])
        if current_tree.right:
            driver(current_tree.right, next_path_sum, next_path[:])

    driver(tree, path_sum, [])
    return result
