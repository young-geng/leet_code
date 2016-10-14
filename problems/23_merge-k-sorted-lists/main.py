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
                heapq.heappush(pq, (head.val, head))

        sentinel = ListNode(None)
        curr = sentinel
        while len(pq) > 0:
            node = heapq.heappop(pq)[1]
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            curr.next = node
            curr = curr.next
        return sentinel.next
