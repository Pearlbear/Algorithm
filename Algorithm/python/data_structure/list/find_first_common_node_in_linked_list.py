from unittest import TestCase
from .find_kth_node_from_end import ListNode


class TestFindFirstCommonNodeInLinkedList(TestCase):
    def test_find_first_common_node_in_linked_list(self):
        common_node = ListNode(6, ListNode(7))
        list1 = ListNode(1, ListNode(2, ListNode(3, common_node)))
        list2 = ListNode(4, ListNode(5, common_node))
        self.assertEqual(find_first_common_node_in_linked_list(list1, list2), common_node)


def find_first_common_node_in_linked_list(linked_list1, linked_list2):
    if not (linked_list1 and linked_list2):
        return None

    def length(linked_list):
        count = 0
        current_node = linked_list
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    length_of_list1 = length(linked_list1)
    length_of_list2 = length(linked_list2)

    difference = abs(length_of_list1 - length_of_list2)
    current_node_list1 = linked_list1
    current_node_list2 = linked_list2
    while difference:
        if length_of_list1 > length_of_list2:
            current_node_list1 = current_node_list1.next
        else:
            current_node_list2 = current_node_list2.next
        difference -= 1
    while current_node_list1 and current_node_list2:
        if current_node_list1 is current_node_list2:
            return current_node_list1
        current_node_list1 = current_node_list1.next
        current_node_list2 = current_node_list2.next
    return None
