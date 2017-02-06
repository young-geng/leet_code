# https://leetcode.com/problems/binary-tree-upside-down/?tab=Description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://discuss.leetcode.com/topic/26276/explain-the-question-and-my-solution-python

"""
Recursive algorithm:
Keep finding the leftmost node, make it upside down and
then make its parent to be its rightmost subtree recursively.

GOTCHA: at the last step when you are making original root to be the right node
of the new tree make sure to create another node instead of copying.
"""

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root

        left_root = self.upsideDownBinaryTree(root.left)
        right_most = left_root
        while right_most.right:
            right_most = right_most.right
        # now that we found the right most node, flip it up
        # a one line pythonic assignment, won't work if its multiple lines
        root, right_most.left, right_most.right = left_root, root.right, TreeNode(root.val)
        return root
