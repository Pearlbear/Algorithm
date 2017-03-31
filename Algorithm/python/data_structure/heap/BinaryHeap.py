from unittest import TestCase


class TestBinaryHeap(TestCase):
    def setUp(self):
        self.heap = BinaryHeap()

    def test_insert(self):
        self.heap.insert(1)
        self.assertEqual(self.heap.size(), 1)
        self.heap.insert(2)
        self.assertEqual(self.heap.size(), 2)

    def test_find_min(self):
        self.heap.insert(10)
        self.heap.insert(4)
        self.heap.insert(23)
        self.heap.insert(7)
        self.heap.insert(2)
        self.assertEqual(self.heap.find_min(), 2)
        self.assertEqual(self.heap.size(), 5)

    def test_del_min(self):
        self.heap.insert(10)
        self.heap.insert(4)
        self.heap.insert(23)
        self.heap.insert(7)
        self.heap.insert(2)
        self.assertEqual(self.heap.del_min(), 2)
        self.assertEqual(self.heap.size(), 4)

    def test_is_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.heap.insert(10)
        self.assertFalse(self.heap.is_empty())

    def test_size(self):
        self.assertEqual(self.heap.size(), 0)
        self.heap.insert(10)
        self.assertEqual(self.heap.size(), 1)
        self.heap.insert(11)
        self.assertEqual(self.heap.size(), 2)

    def test_build(self):
        self.heap.build([9, 7, 4, 3, 5, 10])
        self.assertEqual(self.heap.del_min(), 3)
        self.assertEqual(self.heap.del_min(), 4)
        self.assertEqual(self.heap.del_min(), 5)
        self.assertEqual(self.heap.del_min(), 7)
        self.assertEqual(self.heap.del_min(), 9)
        self.assertEqual(self.heap.del_min(), 10)


class BinaryHeap(object):
    def __init__(self):
        self.list = [0]

    def insert(self, value):
        self.list.append(value)
        index = self.size()
        while index > 1:
            parent_index = index // 2
            if self.list[index] < self.list[parent_index]:
                self.list[index], self.list[parent_index] = self.list[parent_index], self.list[index]
                index = parent_index
            else:
                break

    def find_min(self):
        if self.is_empty():
            return None
        return self.list[1]

    def del_min(self):
        if self.is_empty():
            return None
        root = self.list[1]
        self.list[1] = self.list[self.size()]
        self.list.pop()
        self.__down(1)
        return root

    def is_empty(self):
        return len(self.list) <= 1

    def size(self):
        return len(self.list) - 1

    def build(self, value_list):
        self.list = [0] + list(value_list)
        for i in range(self.size() // 2, 0, -1):
            self.__down(i)

    def __min(self, i):
        left_index = 2 * i
        if self.size() == left_index:
            return 2 * i
        elif self.size() > left_index:
            right_index = left_index + 1
            if self.list[left_index] < self.list[right_index]:
                return left_index
            else:
                return right_index
        else:
            return None

    def __down(self, i):
        index = i
        while self.size() >= index * 2:
            min_index = self.__min(index)
            if self.list[index] > self.list[min_index]:
                self.list[index], self.list[min_index] = self.list[min_index], self.list[index]
            index = min_index
