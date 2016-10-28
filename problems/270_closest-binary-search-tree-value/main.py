# https://leetcode.com/problems/closest-binary-search-tree-value/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        # a is upper bound, find closes lower bound in left subtree
        if target < root.val:
            child = root.left
        # a is lower bound, find closest upper bound in right subtree
        else:
            child = root.right

        if not child:
            return a
        # get as close as possible to target,
        # find the node value after root val thats also close to target
        # this creates an implicit range that target --> [a, b] or [b, a]
        b = self.closestValue(child, target)
        # we can make min behave like argmin by passing a function
        return min((a, b), key=lambda v:abs(target-v))
