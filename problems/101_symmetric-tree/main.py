# https://leetcode.com/problems/symmetric-tree/
# Algorithm Explanation
# The key point here is that if root exists. The tree can only be called symmetric
# if left node and right node value are equal to each other. If this is true, we
# need to check the isSymmetric on the left.right and right.left. And finally we
# also need to check left.left and right.right. IF these values exist and equal
# the tree is symmetric. At any time if one value doesnt exist, we say false. If
# neither left nor right exists it is still symmetric.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        # else they both exist so check their values equal or not.
        if left.val != right.val:
            return False
        return self.checkSymmetry(left.right, right.left) and self.checkSymmetry(left.left, right.right)
