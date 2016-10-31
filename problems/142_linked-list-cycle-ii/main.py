# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        p1 = head
        p2 = head
        while p1.next and p1.next.next:
            p1 = p1.next.next
            p2 = p2.next
            # if they meet, they are going to meet somewhere inside cycle
            if p1 == p2:
                # from now on start p1 from head and take one step at a time
                # continue p2, it was inside the cycle, on step at a time
                # when they meet it can be proven that it will be the
                # cycle start node
                p1 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return
