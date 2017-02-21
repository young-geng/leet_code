# https://leetcode.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # create a 2D (mxn) memo table.
        # memo[i][j] refers to number of ways to get to location (i,j)
        # going only right or down.
        # base cases are 1.
        memo = [[1 for x in xrange(n)] for x in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1] # coming from up or left.
        return memo[m-1][n-1]
