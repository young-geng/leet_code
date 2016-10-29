# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, None, None)

    def check(self, root, min_node, max_node):
        if not root:
            return True
        if min_node and root.val <= min_node.val:
            return False
        if max_node and root.val >= max_node.val:
            return False

        left_subtree = self.check(root.left, min_node, root)
        right_subtree = self.check(root.right, root, max_node)

        return left_subtree and right_subtree
