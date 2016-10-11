# https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sofar = nums[0]
        sums = [0]*len(nums)
        sums[0] = nums[0]
        for i in xrange(1, len(nums)):
            sums[i] = max(nums[i], sums[i-1] + nums[i])
            max_sofar = max(max_sofar, sums[i])
        return max_sofar
