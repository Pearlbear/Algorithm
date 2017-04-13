from unittest import TestCase


class TestIsBinarySearchTree(TestCase):
    def test_is_binary_search_tree(self):
        self.assertTrue(is_binary_search_tree([5, 7, 6, 9, 11, 10, 8]))
        self.assertTrue(is_binary_search_tree([5, 6, 9, 11, 10, 8]))
        self.assertTrue(is_binary_search_tree([5, 7, 9, 11, 10, 8]))
        self.assertFalse(is_binary_search_tree([7, 4, 6, 5]))


def is_binary_search_tree(post_order_list):
    if (not post_order_list) or (len(post_order_list) == 1):
        return True
    root = post_order_list[-1]
    i = 0
    for i in range(0, len(post_order_list)):
        if post_order_list[i] > root:
            break
    left = post_order_list[:i]
    right = post_order_list[i:-1]
    for i in left:
        if i > root:
            return False
    for i in right:
        if i < root:
            return False
    return is_binary_search_tree(left) and is_binary_search_tree(right)
