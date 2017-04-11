from unittest import TestCase


class TestFind(TestCase):
    def setUp(self):
        self.list = ListNode(3, ListNode(4, ListNode(5, ListNode(1, ListNode(2)))))

    def test_find(self):
        self.assertEqual(find_kth_node_from_end(self.list, 2), 1)

    def test_find_exception(self):
        self.assertRaises(EmptyListException, find_kth_node_from_end, None, 2)
        self.assertRaises(IndexError, find_kth_node_from_end, self.list, 6)
        self.assertRaises(IndexError, find_kth_node_from_end, self.list, 0)


def find_kth_node_from_end(head_node, k):
    if not head_node:
        raise EmptyListException()
    if k < 1:
        raise IndexError()
    k_pointer = head_node
    last_pointer = head_node
    while k > 1:
        if not last_pointer.next:
            raise IndexError()
        last_pointer = last_pointer.next
        k -= 1
    while last_pointer.next:
        k_pointer, last_pointer = k_pointer.next, last_pointer.next
    return k_pointer.value


class ListNode(object):
    def __init__(self, value, next_node=None):
        self.__value = value
        self.__next = next_node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node


class EmptyListException(Exception):
    pass
