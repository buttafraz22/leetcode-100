# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def sys(root1: Optional[TreeNode], root2:Optional[TreeNode])->bool:
            # base case, leaf nodes
            if not root1 and not root2:
                return True
            # left and right subtrees have different heights
            if not root1 or not root2:
                return False
            # values are not same
            if root1.val != root2.val:
                return False
            # recursive call
            return sys(root1.right, root2.left) and sys(root1.left, root2.right)
        
        return sys(root, root)
        
