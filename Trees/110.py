# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.check(root)
    
        
    def depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    
    def balance(self, root):
        if root is None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)

        if -1 <= l - r <= 1:
            return True
        else:
            return False

    def check(self, root):
        if root is None:
            return True
        balanced = self.balance(root)
        if not balanced:
            return False
        
        return self.check(root.left) and self.check(root.right)
