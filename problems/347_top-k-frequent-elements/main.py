# https://leetcode.com/problems/top-k-frequent-elements/

from collections import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter()
        for elem in nums:
            cnt[elem] += 1
        return map(lambda x: x[0], cnt.most_common(k))
