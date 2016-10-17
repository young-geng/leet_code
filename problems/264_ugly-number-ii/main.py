# https://leetcode.com/problems/ugly-number-ii/
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def addToHeap(heap, dictionary, key):
            if key in dictionary:
                dictionary[key] += 1
            else:
                dictionary[key] = 1
                heapq.heappush(heap, key)

        if n == 1:
            return 1
        heap = [1]
        seen = {1:1}
        for i in xrange(1, n):
            root = heapq.heappop(heap)
            u2 = root*2
            u3 = root*3
            u5 = root*5
            addToHeap(heap, seen, u2)
            addToHeap(heap, seen, u3)
            addToHeap(heap, seen, u5)
        return heapq.heappop(heap)
