from unittest import TestCase


class TestDeque(TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_front(self):
        self.assertRaises(NoMoreItemException, self.deque.remove_rear)
        self.deque.add_front('McGrady')
        self.deque.add_front('Kobe')
        self.deque.add_front('Wade')
        self.assertEqual(self.deque.size(), 3)
        self.assertEqual(self.deque.remove_front(), 'Wade')
        self.assertEqual(self.deque.remove_rear(), 'McGrady')

    def test_rear(self):
        self.assertRaises(NoMoreItemException, self.deque.remove_rear)
        self.deque.add_rear('McGrady')
        self.deque.add_rear('Kobe')
        self.deque.add_rear('Wade')
        self.assertEqual(self.deque.size(), 3)
        self.assertEqual(self.deque.remove_rear(), 'Wade')
        self.assertEqual(self.deque.remove_front(), 'McGrady')

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())
        self.deque.add_front('McGrady')
        self.assertFalse(self.deque.is_empty())
        self.deque.remove_front()
        self.assertTrue(self.deque.is_empty())

    def test_size(self):
        self.assertEqual(self.deque.size(), 0)
        self.deque.add_front('McGrady')
        self.assertEqual(self.deque.size(), 1)
        self.deque.add_front('Kobe')
        self.assertEqual(self.deque.size(), 2)
        self.deque.remove_front()
        self.assertEqual(self.deque.size(), 1)


class Deque(object):
    def __init__(self):
        self.__head = None
        self.__rear = None
        self.__size = 0

    def add_front(self, item):
        node = self.Node(item)
        self.__size += 1
        if self.__head:
            last_head = self.__head
            last_head.last = node
            node.next = last_head
            self.__head = node
        else:
            self.__head = node
            self.__rear = node

    def remove_front(self):
        if not self.__head:
            raise NoMoreItemException()
        self.__size -= 1
        if self.__head is self.__rear:
            value = self.__head.value
            self.__head = None
            self.__rear = None
            return value
        else:
            node = self.__head
            self.__head = node.next
            self.__head.last = None
            return node.value

    def add_rear(self, item):
        node = self.Node(item)
        self.__size += 1
        if self.__rear:
            last_rear = self.__rear
            last_rear.next = node
            node.last = last_rear
            self.__rear = node
        else:
            self.__head = node
            self.__rear = node

    def remove_rear(self):
        if not self.__rear:
            raise NoMoreItemException()
        self.__size -= 1
        if self.__head is self.__rear:
            value = self.__rear.value
            self.__head = None
            self.__rear = None
            return value
        else:
            node = self.__rear
            self.__rear = node.last
            self.__rear.next = None
            return node.value

    def is_empty(self):
        return not self.__head

    def size(self):
        return self.__size

    class Node(object):
        def __init__(self, value, next_node=None, last_node=None):
            self.__value = value
            self.next = next_node
            self.last = last_node

        @property
        def value(self):
            return self.__value


class NoMoreItemException(Exception):
    pass
