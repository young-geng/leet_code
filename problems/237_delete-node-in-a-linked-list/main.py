# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Clever trick: Just modify the values of the node with the next node.
And dont touch any other shit.
"""

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node.next:
            return
        node.val = node.next.val
        node.next = node.next.next
