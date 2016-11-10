# https://leetcode.com/problems/ransom-note/
# easy question
# keep a hashtable of counts of chars in ransom note and magazine.
# if ransom note requires more count for atleast 1 char than the magazine has
# return False, but True otherwise.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_counts = {}
        for c in magazine:
            if not magazine_counts.get(c, None):
                magazine_counts[c] = 1
            else:
                magazine_counts[c] += 1
        for c in ransomNote:
            # return the count left in the dictionary matching that char
            count = magazine_counts.get(c, -1)
            if count <= 0:
                return False
            magazine_counts[c] -= 1
        return True

    # using a Counter object from collections
    import collections
    def canConstructAlternative(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
