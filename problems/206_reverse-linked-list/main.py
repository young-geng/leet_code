# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class RecursiveSolution(object):
    def reverseList(self, head):
        self.reverseListHelper(head, None)

    def reverseListHelper(self, head, prev):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return reverseListHelper(next, head)
            
