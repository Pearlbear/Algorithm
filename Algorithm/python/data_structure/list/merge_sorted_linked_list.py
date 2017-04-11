from unittest import TestCase
from .find_kth_node_from_end import ListNode


class TestMerge(TestCase):
    def test_merge(self):
        linked_list1 = ListNode(1, ListNode(5, ListNode(6, ListNode(11, ListNode(13)))))
        linked_list2 = ListNode(2, ListNode(3, ListNode(6, ListNode(14, ListNode(17)))))
        merged_list = merge_sorted_linked_list(linked_list1, linked_list2)
        current_node = merged_list
        while current_node.next:
            self.assertLessEqual(current_node.value, current_node.next.value)
            current_node = current_node.next

    def test_merge_empty_list(self):
        linked_list1 = ListNode(1, ListNode(5, ListNode(7, ListNode(11, ListNode(13)))))
        linked_list2 = None
        merged_list = merge_sorted_linked_list(linked_list1, linked_list2)
        current_node = merged_list
        while current_node.next:
            self.assertLessEqual(current_node.value, current_node.next.value)
            current_node = current_node.next


def merge_sorted_linked_list(head_node1, head_node2):
    if not head_node1:
        return head_node2
    if not head_node2:
        return head_node1
    if head_node1.value < head_node2.value:
        head_node1.next = merge_sorted_linked_list(head_node1.next, head_node2)
        return head_node1
    else:
        head_node2.next = merge_sorted_linked_list(head_node1, head_node2.next)
        return head_node2
