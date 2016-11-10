# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.numsToIndices = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # check if its the first time adding it.
        if val not in self.numsToIndices:
            self.nums.append(val)
            self.numsToIndices[val] = len(self.nums)-1
            return True
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # if the val exists
        # remove it, both from list and dictionary
        # copy the last item into the gap created.
        if val in self.numsToIndices:
            index = self.numsToIndices[val]
            last = self.nums[-1]
            # copy last item to removed place
            self.nums[index] = last
            # update the last item's index
            self.numsToIndices[last] = index
            # remove the val from dictionary
            self.nums.pop()
            del self.numsToIndices[val]
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        random_index = random.randint(0, len(self.nums)-1)
        return self.nums[random_index]
