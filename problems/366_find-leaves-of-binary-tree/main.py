# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dictionary = defaultdict(list)
        self.calc_height(root, dictionary)
        return [dictionary[k] for k in xrange(len(dictionary))]


    def calc_height(self, root, levels_map):
        if not root:
            return -1
        left_height = self.calc_height(root.left, levels_map)
        right_height = self.calc_height(root.right, levels_map)
        level = 1 + max(left_height, right_height)
        levels_map[level].append(root.val)
        return level
