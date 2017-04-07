from unittest import TestCase
from ..queue.Queue import Queue


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('McGrady')
        self.stack.push('Kobe')
        self.stack.push('Carter')
        self.assertIs('Carter', self.stack.pop())
        self.stack.push('Iverson')
        self.assertIs('Iverson', self.stack.pop())
        self.assertIs('Kobe', self.stack.pop())
        self.assertIs('McGrady', self.stack.pop())


class Stack(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        if not self.queue1.is_empty():
            self.queue1.enqueue(item)
        else:
            self.queue2.enqueue(item)

    def pop(self):
        if not self.queue1.is_empty():
            while self.queue1.size() > 1:
                self.queue2.enqueue(self.queue1.dequeue())
            return self.queue1.dequeue()
        else:
            while self.queue2.size() > 1:
                self.queue1.enqueue(self.queue2.dequeue())
            return self.queue2.dequeue()
