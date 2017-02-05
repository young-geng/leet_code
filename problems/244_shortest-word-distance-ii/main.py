# https://leetcode.com/problems/shortest-word-distance-ii/
### FANTASTIC QUESTION ####


# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?
#
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
"""
Idea is that by storing a hashtable that maps the word -> [indices] we only
need to walk the giant list only ONCE at the beginning. After that for every
query:
* get word1 indices list as list1
* get word2 indices list as list2
walk both lists to find the pair of indices that has the minimum distance

ONE IMPORTANT point here is that we added these indices to our lists in ORDER
so the indices themselves are sorted. Essentially the problem now becomes
find the two indices i, j in sorted arrays A and B such that dist(i, j) is
minimized. This can be solved in linear time. In fact it is going to be
dependent on the list with the smaller length.

Warm uptime: O(N)
Query time: O(N)
Space: O(N)
"""
from collections import defaultdict

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word2indices = defaultdict(list)
        for i,w in enumerate(words):
            self.word2indices[w].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.word2indices[word1], self.word2indices[word2]
        len1, len2 = len(l1), len(l2)
        i, j = 0, 0
        min_sofar = float('inf')
        while i < len1 and j < len2:
            min_sofar = min(min_sofar, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return min_sofar

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
