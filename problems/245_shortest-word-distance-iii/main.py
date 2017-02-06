# https://leetcode.com/problems/shortest-word-distance-iii/

# This is a follow up of Shortest Word Distance. The only difference is now word1
# could be the same as word2.

"""
Without changing much of the previous algorithm we can keep a flag up
if they are the same number. As usual way i1 and i2 will keep track of the words
last seen indices EXCEPT when they are the same make sure i1 = i2 when changing
i2 will make sure that i1 will point to the previous one.
"""

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1, i2 = -1, -1
        min_sofar = len(words)
        is_same = False

        if word1 == word2:
            is_same = True

        for i in xrange(len(words)):
            if words[i] == word1:
                i1 = i

            if words[i] == word2:
                if is_same:
                    i1 = i2
                i2 = i
            if i1 != -1 and i2 != -1:
                min_sofar = min(min_sofar, abs(i1 - i2))
        return min_sofar
