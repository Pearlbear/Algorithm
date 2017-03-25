from .Queue import Queue
from unittest import TestCase


class TestHotPotato(TestCase):
    def test_hot_potato(self):
        self.assertEqual(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7), "Kent")


def hot_potato(names, count):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    total_count = 0
    while queue.size() > 1:
        total_count += 1
        name = queue.dequeue()
        if total_count % count != 0:
            queue.enqueue(name)
    return queue.dequeue()
