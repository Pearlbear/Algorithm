from unittest import TestCase


class TestLinkedList(TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_add(self):
        self.list.add('McGrady')
        self.assertFalse(self.list.is_empty())

    def test_remove(self):
        self.list.add('McGrady')
        self.list.add('Kobe')
        self.list.remove('McGrady')
        self.assertEqual(self.list.size(), 1)

    def test_search(self):
        self.assertFalse(self.list.search('McGrady'))
        self.list.add('McGrady')
        self.list.add('Kobe')
        self.assertTrue(self.list.search('McGrady'))

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.add('McGrady')
        self.assertFalse(self.list.is_empty())

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.add('McGrady')
        self.assertEqual(self.list.size(), 1)
        self.list.add('Kobe')
        self.assertEqual(self.list.size(), 2)

    def test_append(self):
        self.list.append('McGrady')
        self.list.append('Kobe')
        self.assertEqual(self.list.index('Kobe'), 1)

    def test_index(self):
        self.list.add('McGrady')
        self.list.add('Kobe')
        self.assertEqual(self.list.index('Kobe'), 0)
        self.assertEqual(self.list.index('McGrady'), 1)
        self.assertEqual(self.list.index('Wade'), -1)


class TestNode(TestCase):
    def test_value(self):
        first_node = Node('McGrady')
        self.assertEqual(first_node.value, 'McGrady')

    def test_next(self):
        first_node = Node('McGrady')
        second_node = Node('Kobe')
        first_node.next = second_node
        self.assertIs(first_node.next, second_node)


class LinkedList(object):
    def __init__(self):
        self.__head = None

    def add(self, item):
        new_head = Node(item)
        new_head.next = self.__head
        self.__head = new_head

    def remove(self, item):
        current = self.__head
        previous = None
        while current:
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
        while current:
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

    def append(self, item):
        new_node = Node(item)
        current = self.__head
        previous = None
        while current:
            previous = current
            current = current.next
        if not previous:
            self.__head = new_node
        else:
            previous.next = new_node

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
