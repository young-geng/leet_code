# https://leetcode.com/problems/paint-house/

# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain color
# is different. You have to paint all the houses such that no two adjacent houses
# have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3
# costs matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and so
# on... Find the minimum cost to paint all houses.

"""
Dynamic Programming : VITERBI ALGORITHM

This problem is a classic DP problem. At house i+1 we have 3 choices.
We can paint in Red, Green or Blue for each of these choices we have our
recursive problem:

    current_red = min(prev_blue, prev_green) + costs[i+1][0]

Similarly for green and for blue...

Initialization:
prev_red = costs[0][0]
prev_blue = costs[0][1]
prev_green = costs[0][2]
"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        N = len(costs)
        # initializations
        prev_red = costs[0][0]
        prev_blue = costs[0][1]
        prev_green = costs[0][2]

        for i in xrange(1, N):
            current_red = min(prev_green, prev_blue) + costs[i][0]
            current_blue = min(prev_red, prev_green) + costs[i][1]
            current_green = min(prev_red, prev_blue) + costs[i][2]
            prev_red = current_red
            prev_blue = current_blue
            prev_green = current_green

        return reduce(min, [prev_red, prev_blue, prev_green])
