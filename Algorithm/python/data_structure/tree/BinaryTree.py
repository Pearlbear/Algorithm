from unittest import TestCase


class TestBinaryTree(TestCase):
    def setUp(self):
        self.tree = BinaryTree('a')

    def test_constructor(self):
        self.assertEqual(self.tree.key, 'a')

    def test_left(self):
        self.tree.left = BinaryTree('b')
        self.assertEqual(self.tree.left.key, 'b')

    def test_right(self):
        self.tree.right = BinaryTree('c')
        self.assertEqual(self.tree.right.key, 'c')


class BinaryTree(object):
    def __init__(self, key, left=None, right=None):
        self.__key = key
        self.__left = left
        self.__right = right

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right
