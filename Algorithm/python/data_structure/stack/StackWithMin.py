from unittest import TestCase


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertRaises(EmptyStack, self.stack.min)
        self.stack.push(99)
        self.assertEqual(self.stack.min(), 99)
        self.stack.push(12)
        self.assertEqual(self.stack.min(), 12)
        self.stack.push(55)
        self.assertEqual(self.stack.min(), 12)
        self.stack.push(12)
        self.assertEqual(self.stack.min(), 12)
        self.stack.push(5)
        self.assertEqual(self.stack.min(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.min(), 12)
        self.stack.pop()
        self.assertEqual(self.stack.min(), 12)
        self.stack.pop()
        self.assertEqual(self.stack.min(), 12)
        self.stack.pop()
        self.assertEqual(self.stack.min(), 99)


class Stack(object):
    def __init__(self):
        self.__items = None
        self.__min = None

    def push(self, item):
        if not self.__items:
            node = self.Node(item)
            self.__items = node
            self.__min = node
        else:
            node = self.Node(item, self.__items)
            self.__items = node
            if item <= self.__min.value:
                min_node = self.Node(item, self.__min)
                self.__min = min_node

    def pop(self):
        if not self.__items:
            return None
        value = self.__items.value
        self.__items = self.__items.next
        if value == self.__min.value:
            self.__min = self.__min.next
        return value

    def min(self):
        if not self.__min:
            raise EmptyStack()
        return self.__min.value

    class Node(object):
        def __init__(self, value, next_node=None):
            self.__value = value
            self.__next = next_node

        @property
        def value(self):
            return self.__value

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, next_node):
            self.__next = next_node

        def __le__(self, other):
            return self.__value <= other.value


class EmptyStack(Exception):
    pass
