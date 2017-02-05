# https://leetcode.com/problems/nested-list-weight-sum-ii/

# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.
# Example 1:
# Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)
# Example 2:
# Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
"""
This solution utilizes a FIFO Queue to do BFS on the elements.
Keep  a prev and total variables starting both from 0.
First add every element inside nestedList into a queue.
While queue is not empty do:
* get level size until you go through that level:
** Pop an element if its an integer add it to prev
** if its a nested list, parse it and add its elements to queue
* after level is finished, add prev to total by total += prev
This way root level elements will be added multiple times because they are
the first ones to be added to total and total will keep adding itself as well
as the next level after each level. So no reason to keep track of the depth.

RunTime: BFS Runtime O(N) where N is the number of integers.
Space: O(N)
"""


import Queue

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0

        queue = Queue.Queue()
        for e in nestedList:
            queue.put(e)

        prev, total = 0, 0
        while not queue.empty():
            level_size = queue.qsize()
            for i in xrange(level_size):
                e  = queue.get()
                if e.isInteger():
                    prev += e.getInteger()
                else:
                    nested_list = e.getList()
                    for n in nested_list:
                        queue.put(n)
            total += prev
        return total
