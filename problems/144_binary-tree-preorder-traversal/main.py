# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst, stack = [], []
        while True:
            while root:
                lst.append(root.val)
                stack.append(root)
                root = root.left

            if len(stack) == 0:
                return lst
            node = stack.pop()
            root = node.right

        # Alternative Solution
        # lst, stack = [], []
        # while root:
        #     lst.append(root.val)
        #     # store the only right node for later traversal, if it exists
        #     if root.right:
        #         stack.append(root.right)
        #
        #     root = root.left
        #     if not root and len(stack) > 0:
        #         root = stack.pop()
        # return lst
