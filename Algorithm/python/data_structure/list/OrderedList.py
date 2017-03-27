from unittest import TestCase


class TestList(TestCase):
    def setUp(self):
        self.list = OrderedList()

    def test_add(self):
        self.list.add(79)
        self.list.add(12)
        self.list.add(32)
        self.list.add(97)
        self.assertEqual(self.list.size(), 4)
        self.assertEqual(self.list.index(12), 0)
        self.assertEqual(self.list.index(32), 1)
        self.assertEqual(self.list.index(79), 2)
        self.assertEqual(self.list.index(97), 3)

    def test_remove(self):
        self.list.add(97)
        self.list.add(12)
        self.list.remove(12)
        self.assertEqual(self.list.size(), 1)

    def test_search(self):
        self.assertFalse(self.list.search(12))
        self.list.add(79)
        self.list.add(12)
        self.assertTrue(self.list.search(12))

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(33)
        self.assertFalse(self.list.is_empty())

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add(12)
        self.assertEqual(self.list.size(), 1)
        self.list.add(23)
        self.assertEqual(self.list.size(), 2)

    def test_index(self):
        self.list.add(23)
        self.list.add(79)
        self.list.add(12)
        self.assertEqual(self.list.index(12), 0)
        self.assertEqual(self.list.index(23), 1)
        self.assertEqual(self.list.index(79), 2)


class OrderedList(object):
    def __init__(self):
        self.__head = None

    def add(self, item):
        new_node = Node(item)
        if self.__head:
            current = self.__head
            previous = None
            while current and current.value < item:
                previous = current
                current = current.next
            if previous:
                previous.next = new_node
                new_node.next = current
            else:
                new_node.next = self.__head
                self.__head = new_node
        else:
            self.__head = new_node

    def remove(self, item):
        current = self.__head
        previous = None
        while current and current.value <= item:
            if current.value == item:
                break
            previous = current
            current = current.next
        if not previous:
            self.__head = current.next
        else:
            previous.next = current.next

    def search(self, item):
        current = self.__head
        while current and current.value <= item:
            if current.value == item:
                return True
            current = current.next
        return False

    def is_empty(self):
        return not self.__head

    def size(self):
        count = 0
        current = self.__head
        while current:
            current = current.next
            count += 1
        return count

    def index(self, item):
        count = 0
        current = self.__head
        while current:
            if current.value == item:
                return count
            count += 1
            current = current.next
        return -1


class Node(object):
    def __init__(self, value, next_node=None):
        self.__value = value
        self.next = next_node

    @property
    def value(self):
        return self.__value