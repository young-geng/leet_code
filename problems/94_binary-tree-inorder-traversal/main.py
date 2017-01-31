# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Iterative Implementation which is more challenging

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l, stack = [], []
        while True:
            # add node to stack and go left as much as you can
            # adding them to stack as you go.
            while root:
                stack.append(root)
                root = root.left
            # if node doesnt exists, exit and check if there is
            # anything left to do
            if len(stack) == 0:
                return l
            node = stack.pop()
            l.append(node.val)
            root = node.right

    def recursive(self, root):
        if not root:
            return []
        return self.recursive(root.left) + [root.val] + self.recursive(root.right)
