# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        lst = []
        def inorder(root, lst):
            if root is None:
                return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
            return lst
    return inorder(root, lst)[k-1]

    def iterativekthSmallest(self, root, k):
        l, stack = [], []
        while len(l) < k:
            while root:
                stack.append(root)
                root = root.left

            if len(stack) == 0:
                return
            node = stack.pop()
            l.append(node.val)
            root = node.right

        return l[-1]
