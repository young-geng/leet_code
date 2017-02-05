# https://leetcode.com/problems/shortest-word-distance/
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1, i2 = -1, -1
        min_sofar = len(words)
        for i in xrange(len(words)):
            if words[i] == word1:
                i1 = i
            if words[i] == word2:
                i2 = i
            if i1 and i2:
                min_sofar = min(min_sofar, abs(i1 - i2))
        return min_sofar


class NaiveSolution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_sofar = len(words)
        for i in xrange(len(words)):
            if words[i] == word1:
                for j in xrange(len(words)):
                    if words[j] == word2:
                        min_sofar = min(min_sofar, abs(i - j))
        return min_sofar
