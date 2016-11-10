# https://leetcode.com/problems/linked-list-cycle/

# keep two pointers over the list, one is a fast and other is a slow pointer.
# 1) start slow, fast from the same head
# 2) go until you cannot go meaning fast.next and fast.next.next still exists
# 3) each iteration move slow pointer by one, fast pointer by 2 nodes
# 4) if they ever meet then there is a cycle.

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
