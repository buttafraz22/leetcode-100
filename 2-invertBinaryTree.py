# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # This solution has a time complexity of O(n).
        
        def recurse(node):
            """Helper function to define the recursion that inverts the binary tree.

            Args:
                node (TreeNode): TreeNode object of the root.

            Returns:
                TreeNode: Inverted root at that level.
            """
            if node:
                node.left, node.right = recurse(node.right), recurse(node.left)
                return node
        
        recurse(root)
        return root