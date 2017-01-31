# https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = []
        self.backtrack(combinations, [], 1, n, k)
        return combinations

    def backtrack(self, combinations, nums, start, n, k):
        # add the produced combination and start backtracking
        if k == 0:
            combinations.append(nums)

        for i in xrange(start, n+1):
            nums.append(i)
            self.backtrack(combinations, nums, start+1, n, k-1)
            nums.pop()
