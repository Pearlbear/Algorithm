from unittest import TestCase
from ..stack.Stack import Stack


class TestQueue(TestCase):
    def test(self):
        queue = Queue()
        queue.enqueue('McGrady')
        queue.enqueue('Kobe')
        queue.enqueue('Carter')
        self.assertIs('McGrady', queue.dequeue())
        self.assertIs('Kobe', queue.dequeue())
        queue.enqueue('Iverson')
        queue.enqueue('Wade')
        self.assertIs('Carter', queue.dequeue())
        self.assertIs('Iverson', queue.dequeue())
        self.assertIs('Wade', queue.dequeue())



class Queue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
