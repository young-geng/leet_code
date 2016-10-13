# https://leetcode.com/problems/path-sum/
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None and sum - root.val == 0:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum - root.val)
