# https://leetcode.com/problems/wiggle-sort/

# # Algorithm
# Key point here is to realie that between pairs of numbers we want to create
# a relationship:
#     * num[0] <= num[1] >= num[2] <= num[3] >= num[4] <= ...
#
# If we fix the ordering between num[1] and num[0] by swapping them, we dont
# have to be concerned about the ordering of the rest getting invalidated. In
# other words the pairs can be fixed and swapped independent of each other. Only
# thing is that the odd index positions must contain numbers that are larger than
# both of their left and right neighbors. So a GREEDY algorithm should work.

# Walk through the array starting from the index=1 position since index 0 doesnt
# have a number left of it. Let say at any given i
# 1) if i is odd, then check if num[i-1] > num[i] if so, swap it.
# 2) if i is even, then check if num[i-1] < num[i] if so, swap it.
# SO at any time if we swap we always swap with left element.

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            # if odd
            if i % 2 == 1:
                if nums[i-1] > nums[i]:
                    self.swap(nums, i)
            # else its even
            else:
                if nums[i-1] < nums[i]:
                    self.swap(nums, i)

    def swap(self, nums, i):
        nums[i-1], nums[i] = nums[i], nums[i-1]
