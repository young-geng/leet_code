# https://leetcode.com/problems/roman-to-integer/

"""
In roman numerals every char is added starting from beginngin to end. However,
if there is ever a letter which is less than its latter letter then that letter
is subtracted. With the exception of the last letter. Last letter is always added.
Hence the algorithm is simple:
* Iterate over the string s from 0 --> len(s)-2 because we want to handle the last
char right before we return.
Runtime: O(N)
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap = {'M': 1000,
                    'D': 500,
                    'C': 100,
                    'L': 50,
                    'X': 10,
                    'V': 5,
                    'I':1,
        }
        res = 0
        for i in xrange(len(s) - 1):
            if romanMap[s[i]] < romanMap[s[i+1]]:
                res -= romanMap[s[i]]
            else:
                res += romanMap[s[i]]
        res += romanMap[s[-1]]
        return res
