from unittest import TestCase
from .find_kth_node_from_end import ListNode


class TestReverse(TestCase):
    def test_reverse(self):
        linked_list = ListNode(3, ListNode(4, ListNode(5, ListNode(1, ListNode(2)))))
        linked_list = reverse_linked_list(linked_list)
        self.assertEqual(linked_list.value, 2)
        self.assertEqual(linked_list.next.value, 1)
        self.assertEqual(linked_list.next.next.value, 5)
        self.assertEqual(linked_list.next.next.next.value, 4)
        self.assertEqual(linked_list.next.next.next.next.value, 3)
        self.assertIsNone(linked_list.next.next.next.next.next)

    def test_one_node_list_reverse(self):
        linked_list = ListNode(1)
        linked_list = reverse_linked_list(linked_list)
        self.assertEqual(linked_list.value, 1)
        self.assertIsNone(linked_list.next)

    def test_empty_list_reverse(self):
        linked_list = None
        self.assertIsNone(reverse_linked_list(linked_list))


def reverse_linked_list(head_node):
    if not (head_node and head_node.next):
        return head_node
    new_next = None
    current = head_node
    while current:
        new_previous = current.next
        current.next = new_next
        new_next = current
        current = new_previous
    return new_next
