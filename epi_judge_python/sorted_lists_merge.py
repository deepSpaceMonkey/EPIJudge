from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Are these singly or doubly linked list
# If singly iterate until both nodes are null (Book says yes)
# If doubly iterate until both nodes reach head node again
def merge_two_sorted_lists(L1_node: Optional[ListNode],
                           L2_node: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.

    # We are not creating a new List. We are just changing the pointers
    # So the pointers point all over the place between the two lists
    # Tail is there so we build from the back
    # It's important that dummy_head = tail so that it stays as the head

    dummy_head = tail = ListNode()
    while (L1_node is not None) and (L2_node is not None):
        if L1_node.data <= L2_node.data:
            tail.next = L1_node
            L1_node = L1_node.next
        elif L1_node.data > L2_node:
            tail.next = L2_node
            L2_node = L2_node.next
        tail = tail.next

    # Append the last node that is not null (one of them is for certain)
    tail.next = L1_node or L2_node

    dummy_head = dummy_head.next
    return dummy_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
