# https://leetcode.com/problems/find-the-duplicate-number/
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        walker = nums[0]
        runner = nums[nums[0]]
        # they will always meet at some index in the cycle
        while walker != runner:
            walker = nums[walker]
            runner = nums[nums[runner]]
        runner = 0
        while runner != walker:
            walker = nums[walker]
            runner = nums[runner]
        return walker
