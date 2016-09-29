# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        inidices = {}
        for i in xrange(len(nums)):
            # Always preserve the last index
            inidices[nums[i]] = i

        for i in xrange(len(nums)):
            # Find the desired number
            if target - nums[i] in inidices and inidices[target - nums[i]] != i:
                return [i, inidices[target - nums[i]]]
