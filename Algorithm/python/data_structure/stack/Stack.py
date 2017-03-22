from unittest import TestCase


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('McGrady')
        self.assertEqual(self.stack.size(), 1)
        self.stack.push('Kobe')
        self.assertEqual(self.stack.size(), 2)

    def test_pop(self):
        self.assertRaises(NoMoreItemException, self.stack.pop)
        self.stack.push('McGrady')
        self.assertIs('McGrady', self.stack.pop())
        self.assertEqual(self.stack.size(), 0)

    def test_peek(self):
        self.assertRaises(NoMoreItemException, self.stack.peek)
        self.stack.push('McGrady')
        self.assertIs('McGrady', self.stack.peek())
        self.assertEqual(self.stack.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push('McGrady')
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push('McGrady')
        self.assertEqual(self.stack.size(), 1)
        self.stack.push('Kobe')
        self.assertEqual(self.stack.size(), 2)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        raise NoMoreItemException()

    def peek(self):
        if self.items:
            return self.items[-1]
        raise NoMoreItemException()

    def is_empty(self):
        return False if self.items else True

    def size(self):
        return len(self.items)


class NoMoreItemException(Exception):
    pass
