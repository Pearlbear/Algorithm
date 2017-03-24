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
        self.assertIs('McGrady', self.queue.dequeue())
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


class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None
        self.__size = 0

    def enqueue(self, item):
        if self.rear:
            node = self.Node(item)
            self.rear.next = node
            self.rear = node
        else:
            node = self.Node(item)
            self.head = node
            self.rear = node
        self.__size += 1

    def dequeue(self):
        if not self.head:
            raise NoMoreItemException()
        self.__size -= 1
        if self.head is self.rear:
            item = self.head.value
            self.head = None
            self.rear = None
            return item
        else:
            node = self.head
            self.head = node.next
            return node.value

    def is_empty(self):
        return False if self.head else True

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
