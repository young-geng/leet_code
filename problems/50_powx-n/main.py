# https://leetcode.com/problems/powx-n/
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1.0
        abs_n = abs(n)
        while abs_n > 0:
            if (abs_n & 1):
                ans *= x
            abs_n = abs_n >> 1
            x *= x
        if n < 0:
            return 1/ans
        return ans
