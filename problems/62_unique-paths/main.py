# https://leetcode.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = [[1 for x in xrange(n)] for x in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                p[i][j] = p[i-1][j] + p[i][j-1]
        return p[m-1][n-1]
    
