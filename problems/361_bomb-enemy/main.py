# https://leetcode.com/problems/bomb-enemy/

# Here the important thing to recognize is that we only update the number of
# killed enemies in each row and column calculations or we remake those
# calculations if and only if we have met a wall in the previous box. If we are
# simply walking each box and havent met a single wall yet than we calculate
# the enemies can be killed for that row and column and we dont calculate it
# since we are at the same row as we are iterating the columns first. This saves
# us computation of enemies at each location redundantly since if the enemy is
# counted at the previous column for the same row in column+1 the enemy size
# should be the same.


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        max_killed = 0
        rows, cols = len(grid), len(grid[0])
        killed_col = [0]*cols
        for i in xrange(rows):
            for j in xrange(cols):
                # if there is a wall continue.
                if grid[i][j] == "W":
                    continue
                # count enemies in this row from a prospective all and on
                # only count if we have seen a wall in previously
                # store in row_killed for this row
                if j == 0 or grid[i][j-1] == "W":
                    killed_row = self.countKilledInRow(grid, rows, cols, i, j)
                # count enemies in this column and assign it to killed column
                # only count if we have seen a wall previously
                # array.
                if i == 0 or grid[i-1][j] == "W":
                    killed_col[j] = self.countKilledInColumn(grid, rows, cols, i, j)
                # now that we counted prospective enemies on this column and row
                # we will try droppping a bomb and update the max
                if grid[i][j] == "0":
                    num_killed = killed_row + killed_col[j]
                    max_killed = max(max_killed, num_killed)

        return max_killed

    def countKilledInRow(self, grid, rows, cols, i, j):
        # count the enemy number in this row moving from all columns j
        # if we hit a wall we stop
        # if we hit the end of the grid we stop
        killed = 0
        while j < cols and grid[i][j] != "W":
            if grid[i][j] == "E":
                killed += 1
            j += 1
        return killed

    def countKilledInColumn(self, grid, rows, cols, i, j):
        killed = 0
        while i < rows and grid[i][j] != "W":
            if grid[i][j] == "E":
                killed += 1
            i += 1
        return killed
