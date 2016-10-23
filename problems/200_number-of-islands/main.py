# https://leetcode.com/problems/number-of-islands/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        cols,rows = len(grid), len(grid[0])
        def dfs(i, j):
            """
            helper function to start filling every cell reachable from (i,j)
            with '0's. A variation of Flood Fill algorithm for connected
            components.
            """
            if i >= 0 and j >= 0 and i < cols and j < rows:
                # if not visited, mark it '0' and run dfs
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    # vertical move
                    dfs(i-1, j)
                    dfs(i+1, j)
                    # horizontal move
                    dfs(i, j-1)
                    dfs(i, j+1)

        cc_count = 0
        for i in xrange(cols):
            for j in xrange(rows):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cc_count += 1
        return cc_count
