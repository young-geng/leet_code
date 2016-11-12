# https://leetcode.com/problems/moving-average-from-data-stream/

# Algorithm and Design
# --------------------
# Idea is to "emulate" the sliding window
# for this we can simply use deque or a double ended queueu where we can push
# from the head when we encounter something new and we can poop out from the
# tail at the same time to "slide" the window to right.

import collections
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = collections.deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        window.append(val)
        return float(sum(window))/len(window)





# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
