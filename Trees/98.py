# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.BSThelp(root)
    
    def BSThelp(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if root is None:
            return True

        if not (low < root.val < high):
            return False

        l = self.BSThelp(root.left, low, root.val)
        r = self.BSThelp(root.right, root.val, high)

        return l and r
        
