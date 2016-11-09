# https://leetcode.com/problems/word-pattern/

# The idea here is that we can create a bijection between the pattern chars
# and the words in the str and assign them unique values which will be indices
# so if the key already is in the dictionary its value must be the first index it
# appeared. If we encounter a key thats in the dictionary but matched with a
# different index than it must mean we have a mismatch.

# so for example the these mappings:
# pattern: 'abba' --> mapping [0,1,1,0]
# 'dog cat cat dog' -> mapping [0,1,1,0] MATCH
# 'dog cat pig dog' -> mapping [0,1,2,0] MISMATCH

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        # set default returns the value if it exists, if not sets the default
        f = lambda keys: map({}.setdefault, keys, xrange(len(keys)))
        return f(pattern) == f(words)
