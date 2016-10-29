# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = []
        out = []
        q.append(root)
        while len(q) > 0:
            num_level_elements = len(q)
            lst = []
            for i in xrange(num_level_elements):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                lst.append(node.val)
            out.append(lst)
        return out
