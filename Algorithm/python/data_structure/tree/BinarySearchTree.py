from unittest import TestCase


class TestBinarySearchTree(TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_put(self):
        self.assertIsNone(self.tree.get(34))
        self.tree.put(34, 'a')
        self.assertEqual(self.tree.get(34), 'a')
        self.tree.put(34, 'b')
        self.assertEqual(self.tree.get(34), 'b')
        self.assertIsNone(self.tree.get(45))
        self.tree.put(45, 'c')
        self.assertEqual(self.tree.get(45), 'c')


class BinarySearchTree(object):
    def __init__(self):
        self.__root = None
        self.__size = 0

    def put(self, key, value):
        if self.is_empty():
            self.__root = self.Node(key, value)
            self.__size += 1
            return
        else:
            def driver(current):
                if key < current.key:
                    if current.has_left():
                        driver(current.left)
                    else:
                        current.left = self.Node(key, value, parent=current)
                        self.__size += 1
                elif key > current.key:
                    if current.has_right():
                        driver(current.right)
                    else:
                        current.right = self.Node(key, value, parent=current)
                        self.__size += 1
                else:
                    current.value = value
            driver(self.__root)

    def get(self, key):
        if self.is_empty():
            return None
        target = self.__get(key, self.__root)
        return target.value if target else None

    def __get(self, key, current):
        if not current:
            return None
        if current.key == key:
            return current
        elif key < current.key:
            return self.__get(key, current.left)
        else:
            return self.__get(key, current.right)

    def size(self):
        return self.__size

    def is_empty(self):
        return not self.__root

    def __len__(self):
        return self.__size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return not self.get(key)

    class Node(object):
        def __init__(self, key, value, parent=None, left=None, right=None):
            self.__key = key
            self.__value = value
            self.__parent = parent
            self.__left = left
            self.__right = right

        def is_root(self):
            return not self.__parent

        def is_left(self):
            return self.__parent and self.__parent.left is self

        def is_right(self):
            return self.__parent and self.__parent.right is self

        def has_left(self):
            return True if self.__left else False

        def has_right(self):
            return True if self.__right else False

        def is_leaf(self):
            return not (self.__left or self.__right)

        def has_child(self):
            return self.__left or self.__right

        def has_both_child(self):
            return self.__left and self.__right

        @property
        def key(self):
            return self.__key

        @key.setter
        def key(self, key):
            self.__key = key

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        @property
        def parent(self):
            return self.__parent

        @parent.setter
        def parent(self, parent):
            self.__parent = parent

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

