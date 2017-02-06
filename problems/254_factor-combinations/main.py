# https://leetcode.com/problems/factor-combinations/

# Write a function that takes an integer n and return all possible combinations of
# its factors. Factors are always greater than 1 and less than n
#
# Ex1:
# input: 1
# output: []
#
# Ex2:
# input:37
# out: []
#
# Ex3:
# input: 12
# output: [[2,6],
#          [2, 2, 3],
#          [3,4]]


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def factor_helper(num, i, stack, res):
            while i**2 <= num:
                if num % i == 0:
                    stack.append(i)
                    res.append(list(stack) + [num/i])
                    factor_helper(num/i, i, stack, res)
                    stack.pop()
                i += 1
            return res
        return factor_helper(n, 2, [], [])
