# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if node p and q dont exist then True
        if not p and not q:
            return True
        # if one of them doesnt exist return false
        if not p or not q:
            return False
        # else it has the node there so check if the nodes are same
        # check isSame left subtree and check if same right subtree
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
