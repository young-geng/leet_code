# https://leetcode.com/problems/flatten-nested-list-iterator/?tab=Description

"""
    Main idea here is that in constructor make sure to dump items onto a
    stack but iterating from backward of the nestedList to front so that
    when we start popping from stack we can process the elements in the correct
    order.

    This will come up handy later in hasNext() function too so why not make it
    a helper funct call it 'dump_items_to_stack'.

    Whenever someone calls next(), pop item from the stack and we will
    enforce the invariant that it will always be an integer.

    To enforce this, it must be done in the hasNext() function. Whenever we call
    hasNext() we will peek at the stack:
    * Return True if its an integer
    * Dump elements of it to stack if its a nestedList.

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = deque()
        self.dump_items_to_stack(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            e = self.stack.pop()
            self.dump_items_to_stack(e.getList())
        return False

    def dump_items_to_stack(self, nested_list):
        # dump from backwards of nestedList since
        # we want to preserve the inner list order.
        for i in xrange(len(nested_list)-1, -1, -1):
            self.stack.append(nested_list[i])

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
