# https://leetcode.com/problems/group-shifted-strings/

import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            key = tuple((ord(c)-ord(s[0])) % 26 for c in s)
            groups[key].append(s)
        print groups
        return map(sorted, groups.values())
