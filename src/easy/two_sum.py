"""
Two Sum
=======
Tags: Junior, Array, Hash Table

Description
-----------
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Solution
--------
Create a hash table of the currently selected number and the difference between
the target value and currently selected number. If the difference value appears
as a key in the hash table, then both the current number at the key value are the
solution
"""

from typing import List


# ========================================
# SOLUTION
# ========================================
def two_sum(nums: List[int], target: int) -> List[int]:
    store = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in store:
            return [nums.index(diff), i]
        store[num] = diff


# ========================================
# TESTS
# ========================================
def test_1():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_2():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_3():
    assert two_sum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 1], 2))
