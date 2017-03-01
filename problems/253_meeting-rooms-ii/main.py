# https://leetcode.com/problems/meeting-rooms-ii/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class MyHeap(object):
    def __init__(self, initial=None, key=lambda x:x):
        self.key = key
        if initial:
            self._data = [(key(item),item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []
    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def size(self):
        return len(self._data)


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0: return 0

        pq = MyHeap(key=lambda t: t.end)
        # sort intervals by start times
        intervals = sorted(intervals, key=lambda i: i.start)
        pq.push(intervals[0])
        for current in intervals[1:]:
            # get the meeting room that finishes first
            earliest = pq.pop()
            # if the current meeting starts right after the earliest finishes,
            # no need for a new room, just use the same room, so extend the
            # meeting room timeslot
            if current.start >= earliest.end:
                earliest.end = current.end
            # otherwise the current meeting needs a new room
            # add new room to heap
            else:
                pq.push(current)
            # put the earliest back to the heap to keep track of that room
            pq.push(earliest)

        return pq.size()
