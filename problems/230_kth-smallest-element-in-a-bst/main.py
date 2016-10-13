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
