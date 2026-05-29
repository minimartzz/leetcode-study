"""
Two Sum
=======
Tags: Principal, Linked List, Math, Recursion

Description
-----------
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Solution
--------
Create a hash table of the currently selected number and the difference between
the target value and currently selected number. If the difference value appears
as a key in the hash table, then both the current number at the key value are the
solution
"""

from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ========================================
# SOLUTION
# ========================================
def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    start = ListNode(0)
    temp = start
    add = 0

    while l1 or l2 or add:
        val = start.val
        val += add
        add = 0

        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        add, remainder = divmod(val, 10)

        temp.next = ListNode(remainder)
        temp = temp.next

    return start.next


# ========================================
# HELPERS
# ========================================
def list_to_linked_list(rl: list[int]) -> Optional[ListNode]:
    temp = ListNode(0)
    curr = temp
    for n in rl:
        curr.next = ListNode(n)
        curr = curr.next
    return temp.next


def linked_list_to_list(ll: Optional[ListNode]) -> list[int]:
    rl = []
    while ll:
        rl.append(ll.val)
        ll = ll.next
    return rl


# ========================================
# TESTS
# ========================================
@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9, 9, 9], [0, 0, 0, 1]),
        (
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
            [5, 6, 4],
            [
                6,
                6,
                4,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ],
        ),
    ],
    ids=[
        "Leetcode test 1",
        "Leetcode test 2",
        "Leetcode test 3",
        "Edge case 1",
        "Edge case 2",
    ],
)
def test_add_two_numbers(l1, l2, expected):
    result = add_two_numbers(list_to_linked_list(l1), list_to_linked_list(l2))
    assert linked_list_to_list(result) == expected


if __name__ == "__main__":
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    res = add_two_numbers(l1, l2)
    print(linked_list_to_list(res))
