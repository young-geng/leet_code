# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for head in lists:
            if head != None:
                # push all heads of every list into our PriorityQueue
                # push in a tuple s.t it can be sorted by the first elem of
                # the tuple
                heapq.heappush(pq, (head.val, head))

        sentinel = ListNode(None)
        curr = sentinel
        # when there are still things to add in PQ
        while len(pq) > 0:
            # get the smallest node in PQ
            node = heapq.heappop(pq)[1]
            # if node has a next node, add it to our PQ to be processed later
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            curr.next = node
            curr = curr.next
        return sentinel.next
