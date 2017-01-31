# https://leetcode.com/problems/longest-palindrome/

"""
Idea here is that go thorugh the string char by char while doing it keep a dict
of char counts.
For each char:
    * check if it exists in dictionary, if it does pop it because it means we
    found 2 same chars. Increment the count by one.
    * if it doesnt exist, add it to dictionary.

At the end the dict will only contain odd items as they will only be added and
never will get popped. This means we can construct a palindrome by using all the
even pairs and just one odd char in the middle. return 2*counter + 1

If the dict got emptied out which means the string only contained chars with
even counts then return 2*count.

Runtime:
O(N)
"""

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars_dictionary = defaultdict(int)
        count = 0
        for char in s:
            # pop the char and return val which is 0 if it doesnt exist.
            val = chars_dictionary.pop(char, 0)
            if val:
                count += 1
            else:
                # if doesnt exist put the char in the dict increment value
                chars_dictionary[char] += 1

        if len(chars_dictionary):
            return 2*count + 1

        return 2*count
