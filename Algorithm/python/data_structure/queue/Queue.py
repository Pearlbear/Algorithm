from unittest import TestCase


class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('McGrady')
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue('Kobe')
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue(self):
        self.assertRaises(NoMoreItemException, self.queue.dequeue)
        self.queue.enqueue('McGrady')
        self.queue.enqueue('Kobe')
        self.assertIs('McGrady', self.queue.dequeue())
        self.assertIs('Kobe', self.queue.dequeue())
        self.assertEqual(self.queue.size(), 0)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('McGrady')
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue('McGrady')
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue('Kobe')
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)


class Queue(object):
    def __init__(self):
        self.__head = None
        self.__rear = None
        self.__size = 0

    def enqueue(self, item):
        node = self.Node(item)
        self.__size += 1
        if self.__rear:
            self.__rear.next = node
            self.__rear = node
        else:
            self.__head = node
            self.__rear = node

    def dequeue(self):
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
            return node.value

    def is_empty(self):
        return not self.__head

    def size(self):
        return self.__size

    class Node(object):
        def __init__(self, value, next_node=None):
            self.__value = value
            self.next = next_node

        @property
        def value(self):
            return self.__value


class NoMoreItemException(Exception):
    pass
