# https://leetcode.com/problems/first-missing-positive/

"""
Similar to Bloomberg's question for Brian.
In this quesiton I am using the invariant that A[i] should contain value i+1
Rest is this explanation:

Time: O(N)
Space: O(1)

http://stackoverflow.com/questions/1586858/find-the-smallest-integer-not-in-a-list
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        for i in xrange(N):
            number = nums[i]
            while number in xrange(1, N+1) and number != nums[number - 1]:
                swapped = nums[number-1]
                nums[number-1] = number
                number = swapped

        for i in xrange(N):
            if nums[i] != i+1:
                return i+1
        # after all else it must have been N+1 because we put everything in
        # their rightful places.
        return N+1
