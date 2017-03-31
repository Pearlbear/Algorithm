from unittest import TestCase


class TestBinaryTree(TestCase):
    def setUp(self):
        self.tree = BinaryTree('a')

    def test_constructor(self):
        self.assertEqual(self.tree.key, 'a')

    def test_left(self):
        self.tree.left = 'b'
        self.assertEqual(self.tree.left.key, 'b')

    def test_right(self):
        self.tree.right = 'c'
        self.assertEqual(self.tree.right.key, 'c')


class BinaryTree(object):
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None

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
        if self.__left:
            new_left = BinaryTree(left)
            new_left.left = self.__left
            self.__left = new_left
        else:
            self.__left = BinaryTree(left)

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if self.__right:
            new_right = BinaryTree(right)
            new_right.right = self.__right
            self.__right = new_right
        else:
            self.__right = BinaryTree(right)
