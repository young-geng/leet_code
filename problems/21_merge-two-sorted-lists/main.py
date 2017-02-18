# https://leetcode.com/problems/merge-two-sorted-lists/?tab=Description

"""
Merge two linked lists that are sorted.

Keep a dummy node which comes before the beginning of the list.
Keep a curr pointer to assign sorted nodes to each other.
In the end think a little and return.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # this step is neccessary because if l1 or l2 is shorter
        # curr will end at the end of l1 or l2 and will take over the leftout.
        curr.next = l1 or l2
        return dummy.next
