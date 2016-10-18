# https://leetcode.com/problems/merge-intervals/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def is_overlapping(source, target):
            # hard overlap
            return target.start <= source.end

        def merge_two(i1, i2):
            start = i1.start if i1.start <= i2.start else i2.start
            end = i1.end if i1.end >= i2.end else i2.end
            return Interval(start, end)

        if len(intervals) == 0: return []

        output = []
        intervals = sorted(intervals, key=lambda e: e.start)
        current = intervals[0]
        for interval in intervals[1:]:
            if is_overlapping(current, interval):
                current = merge_two(current, interval)
            else:
                output.append(current)
                current = interval
        output.append(current)
        return output
