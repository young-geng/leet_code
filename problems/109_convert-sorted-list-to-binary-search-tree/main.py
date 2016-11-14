# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # instead of always walking to the middle of linked list, we will
        # solve it with a bottom up recursive approach similar to how we do
        # backtracking from left node. We will have to walk the list to decide
        # how long it is at first.
        curr = head
        n = 0 # length of the linked list
        while curr:
            n += 1
            curr = curr.next
        return self.createTree(head, 0, n-1)

    # very similar to the previous idea.
    # recursively construct the tree
    # starting from left most node.
    def createTree(self, node, start, end):
        if start > end:
            return
        mid = (start + end)/2
        leftChild = self.createTree(node, start, mid-1)
        parent = TreeNode(node.val)
        parent.left = leftChild
        node = node.next
        parent.right = self.createTree(node, mid+1, end)
        return parent
