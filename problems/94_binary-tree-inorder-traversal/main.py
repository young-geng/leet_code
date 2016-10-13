# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Iterative Implementation which is more challenging

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                return l
            node = stack.pop()
            l.append(node.val)
            root = node.right
