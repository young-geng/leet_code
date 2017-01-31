# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        for i in xrange(len(nums)):
            # Always preserve the last index
            indices[nums[i]] = i

        for i in xrange(len(nums)):
            # Find the desired number
            desired_num = target - nums[i]
            if desired_num in indices and indices[desired_num] != i:
                return [i, indices[desired_num]]
