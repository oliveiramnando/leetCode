# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, root.val)
        
    def count(self, root, val):
        if root is None:
            return 0
        
        if root.val >= val:
            val = root.val
            return 1 + self.count(root.left, val) + self.count(root.right, val)
        else:
            return self.count(root.left, val) + self.count(root.right, val)

