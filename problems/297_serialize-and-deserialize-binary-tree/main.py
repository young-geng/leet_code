# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_helper(root, s):
            if not root:
                return "X" + ","
            s = str(root.val) + ","
            s += serialize_helper(root.left, s)
            s += serialize_helper(root.right, s)
            return s
        return serialize_helper(root, "")


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = []
        nodes.extend(data.split(","))
        return self.build_tree(nodes)

    def build_tree(self, nodes):
        """
        helper method to build the tree.
        Args:
        - nodes: list[str] of node values serialized
        Output:
        - node: TreeNode denoting the root of tree.
        """
        val = nodes.pop(0)
        if val == "X":
            return
        root = TreeNode(int(val))
        root.left = self.build_tree(nodes)
        root.right = self.build_tree(nodes)
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
