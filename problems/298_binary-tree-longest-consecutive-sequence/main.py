# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This algorithm is basically a graph DFS algorithm that traverses the tree
# using **iteration**. In the stack we not only append parent node and its
# children but we also keep track of the length of longest consecutive sequence
# that could be made using that node. By popping it off from stack we know that
# it will be a parent node when adding new items to stack we just have to make
# sure to add the lengths of consecutive sequences correctly.
# When popping a node to visit from stack make sure to update the new max_sofar
# variable that keeps track of len of maximum consecutive sequence.

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_sofar = 0
        stack = [[root, 1]]
        while stack:
            node, length = stack.pop()
            max_sofar = max(max_sofar, length)
            for child in [node.left, node.right]:
                if child:
                    if child.val == node.val + 1:
                        l = length + 1
                    else:
                        l = 1
                    stack.append([child, l])
        return max_sofar
