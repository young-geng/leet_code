# https://leetcode.com/problems/binary-tree-postorder-traversal/?tab=Description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Implementation will use TWO STACKS.
While stack1 is not empty:
* Pop front of the stack. Add it to the second stack.
* If it has children, add them to the stack one. First left than right.

Return second stack.

To make things simpler and more efficient, I will use a deque data structure.

RunTime: O(N)
"""

from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack1 = deque()
        stack2 = deque()
        stack1.append(root)
        while len(stack1):
            node = stack1.popleft()
            stack2.appendleft(node)
            if node.left:
                stack1.appendleft(node.left)
            if node.right:
                stack1.appendleft(node.right)
        return list(stack2)
