# https://leetcode.com/problems/first-unique-character-in-a-string/
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charToCounts = collections.defaultdict(lambda: s.count(c))
        uniques = [i for i, c in enumerate(s) if charToCounts[c] < 2]
        return uniques[0] if uniques else -1
