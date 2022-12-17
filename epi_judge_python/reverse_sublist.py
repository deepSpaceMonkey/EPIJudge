from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(head: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    '''
    Time: O(n); 2 passes
    Space: O(1); in-place
    Notes: This can be optimized for 1 pass. Starting from start_node, reverse
            I didn't do this because it would beef up the while loop which
            would make the code a little more difficult to understand and
            maintain
    Questions: Are we guaranteed that finish < len(LL)?
    '''

    # Edge cases
    if head is None or head.next is None \
            or start >= finish \
            or start < 0 or finish < 0:
        return head

    # Traversal vars
    prev_node, cur_node = None, head
    start_i, finish_i, cur_i = start - 1, finish - 1, 0

    # Pointers to save
    node_before_start = start_node = None
    node_after_finish = finish_node = None

    # Traverse LL to put pointers in place
    while cur_node is not None:
        if cur_i == start_i:
            node_before_start = prev_node
            start_node = cur_node
        elif cur_i == finish_i:
            finish_node = cur_node
            node_after_finish = cur_node.next

        prev_node = cur_node
        cur_node = cur_node.next
        cur_i = cur_i + 1

    # Reverse Sublist
    prev_node = None
    cur_node = start_node
    while cur_node is not node_after_finish:
        # save next node
        next_node = cur_node.next
        # reverse the nodes
        cur_node.next = prev_node
        # Traverse LL
        prev_node = cur_node
        cur_node = next_node

    # Update pointers
    if node_before_start is not None:
        node_before_start.next = finish_node
    if node_after_finish is not None:
        start_node.next = node_after_finish
    else:
        start_node.next = None
    # If entire LL was reversed
    if start_node is head:
        head = finish_node

    return head


if __name__ == '__main__':
    # third = ListNode(3, None)
    # second = ListNode(2, third)
    # first = ListNode(1, second)
    # start = 1
    # finish = 2
    # head = reverse_sublist(first, start, finish)
    # print(head)

    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
