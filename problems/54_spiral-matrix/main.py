# https://leetcode.com/problems/spiral-matrix/?tab=Description
"""
    Solved using four for loops to traverse in cyclic order.
    If there is no cycle can be made then simply traverse that sector using
    a single for loop.
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m, n = len(matrix), len(matrix[0])
        x, y = 0, 0

        # while m > 0 and n > 0
        while m and n:
            # if one row left
            # move left->right
            if m == 1:
                for i in xrange(n):
                    result.append(matrix[x][y])
                    y += 1
                break
            # if one column left
            # move up->down
            elif n == 1:
                for i in xrange(m):
                    result.append(matrix[x][y])
                    x += 1
                break

            else:
                #  top ; move right
                for i in xrange(n-1):
                    result.append(matrix[x][y])
                    y += 1
                # right ; move down
                for i in xrange(m-1):
                    result.append(matrix[x][y])
                    x += 1
                # bottom ; move left
                for i in xrange(n-1):
                    result.append(matrix[x][y])
                    y -= 1
                # left ; move up
                for i in xrange(m-1):
                    result.append(matrix[x][y])
                    x -= 1

                x += 1
                y += 1
                m -= 2
                n -= 2
        return result
