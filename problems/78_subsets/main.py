# https://leetcode.com/problems/subsets/
class Solution(object):
    # iterative solution
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        subset_list = [[]] # start with empty subset
        for i in xrange(len(nums)):
            l = [] # so we dont increase subset_list size as we iterate it.
            for j in xrange(len(subset_list)):
                l.append(subset_list[j] + [nums[i]])
            subset_list.extend(l)
        return subset_list

class Solution(object):
    def subsets(self, nums):
        nums = sorted(nums)
        subset_list = []
        self.backtracking(nums, 0, [], subset_list)
        return subset_list

    def backtracking(self, nums, start, temp, subset_list):
        subset_list.append(temp)
        for i in xrange(start, len(nums)):
            # call it recursively
            self.backtracking(nums, i+1, temp + [nums[i]], subset_list)
