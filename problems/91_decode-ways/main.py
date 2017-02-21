# https://leetcode.com/problems/decode-ways/

"""
    Dynamic Programming

    dp[n] = dp[n-1] + dp[n-2]
    Runtime: O(N)


    Be careful. Our memo array is len(s) + 1 size.
    At each iteration i, we check if s[i-1] is valid and s[i-2:i] is valid

"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        memo = [0 for i in xrange(len(s)+1)]
        # 1 ways to decode a empty string
        memo[0] = 1
        # 1 way if to decode a valid char
        memo[1] = 1 if s[0] != "0" else 0

        for i in xrange(2, len(s)+1):
            if int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                memo[i] += memo[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                memo[i] += memo[i-2]
        return memo[len(s)]
