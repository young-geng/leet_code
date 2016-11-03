# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return 0
        if root.left:
            if not root.left.left and not root.left.right:
                sum += root.left.val
            else:
                sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            sum += self.sumOfLeftLeaves(root.right)
        return sum
