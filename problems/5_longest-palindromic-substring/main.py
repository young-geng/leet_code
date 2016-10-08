# https://leetcode.com/problems/longest-palindromic-substring/
class Solution(object):
    def expandFromCenter(self, s, left, right):
        l,r = left, right
        while (l >= 0 and R < len(s) and (s[l] == s[r])):
            l = l - 1
            r = r + 1
        return l - r - 1
    def longestPalindrome(self, s):
        """
        O(n^2) complexity, O(1) space solution
        Input:
        - s: string

        Output:
            string, which is the longest palindroming substring in s
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        start, end = 0, 0
        for i in xrange(len(s)):
            # palindromes can contain 1 or 2 chars in the middle
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            len_of_palindrome = max(len1, len2)
            if len_of_palindrome > (end - start):
                start = i - (max_len - 1)/2
                end = i + max_len/2
        return s[start : end+1]
