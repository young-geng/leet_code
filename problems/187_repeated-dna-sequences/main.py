# https://leetcode.com/problems/repeated-dna-sequences/
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
from collections import defaultdict

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        pattern_counter = defaultdict(int)
        for i in xrange(len(s)):
            pat = s[i:i+10]
            if pattern_counter[pat] > 0:
                res.add(pat)
            pattern_counter[pat] += 1
        return list(res)
