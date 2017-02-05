# https://leetcode.com/problems/two-sum-iii-data-structure-design/
# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
from collections import defaultdict


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.counter[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.counter.keys():
            to_find = value - num
            # one test case is add(0), add(0), find(0) --> True
            # you have to make sure you have enough numbers to add it up
            if to_find in self.counter and (to_find != num or self.counter[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
