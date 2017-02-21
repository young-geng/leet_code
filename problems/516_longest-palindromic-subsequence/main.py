# https://leetcode.com/problems/longest-palindromic-subsequence/

"""
Dynamic Programming

Go through the array keeping two pointers to denote begin and end of the subarray.
Do this for subarrays size 2, 3, ... ,N

For each of the subarrays we have:

We have the following cases:
LPS[i, i] = 1 ; every single char is a palindrome of itself
LPS[i, j] = 2 if j=i+1 ; sequence only has 2 characters
LPS[i, j] = 2 + LPS[i+1, j-1] if first and last chars the same
LPS[i, j] = max{LPS[i+1,j], LPS[i, j-1]} if first and last chars aren't same

Keep a memo_table where memo_table[i][j] is defined as the length of the
longest palindrome from ith index to jth index in the input string.

Runtime: O(n^2)
Naive Runtime: O(2^n)
Space: O(n^2)
"""
# http://stackoverflow.com/questions/4790522/how-to-find-longest-palindromic-subsequence

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        memo_table = [[0 for x in xrange(N)] for y in xrange(N)]
        # fill the base case, single chars are palindrome of len=1
        for i in xrange(N):
            memo_table[i][i] = 1

        for sub_len in xrange(2, N+1):
            for i in xrange(N - sub_len + 1):
                # get the end char
                j = i + sub_len - 1
                # base case, if the tails are the same
                # but the sublen = 2 so put a 2 in memo table
                if s[i] == s[j] and sub_len == 2:
                    memo_table[i][j] = 2
                # recursive case
                # if tails are the same, general case
                elif s[i] == s[j]:
                    memo_table[i][j] = 2 + memo_table[i+1][j-1]

                # tails chars are different, so the other
                # recursive case
                else:
                    memo_table[i][j] = max(memo_table[i+1][j], memo_table[i][j-1])

        # at the end the result is stored at memo[0][N-1]
        # self.printTable(memo_table)
        return memo_table[0][N-1]

    def printTable(self, table):
        N = len(table)
        for i in xrange(N):
            line = " ".join(map(str, table[i]))
            print line
