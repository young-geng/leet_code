# https://leetcode.com/problems/missing-number/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_nums = reduce(lambda x,y: x ^ y, nums)
        xor_n = reduce(lambda x,y : x ^ y, xrange(len(nums)+1))
        return xor_nums ^ xor_n
