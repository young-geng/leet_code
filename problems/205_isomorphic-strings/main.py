# https://leetcode.com/problems/isomorphic-strings/?tab=Description

# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

# You may assume both s and t have the same length.

"""
This is very similar to the problem 290 - Word Pattern. HOWEVER its also a
little different. For example this test case: (ab, ca) --> True

Idea here is that one we have 2 strings "egg" and "add". For the result to be
true one character in the first string must have a unique mapping to another
char in the second string. For ex: e --> a  ,  g --> d.

And the number of such mappings MUST be the same as the number of diferent
letters in the strings. We can use HashSet.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mappings = set(zip(s, t))
        if len(mappings) == len(set(s)):
            if len(mappings) == len(set(t)):
                return True
        return False
