# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        self.helper(root, node)
        return root
    
    def helper(self, root, node):
        if not root:
            root = node
            return root
        
        if root.left is None and root.right is None:
            if node.val < root.val:
                root.left = self.helper(root.left, node)
            else:
                root.right = self.helper(root.right, node)
            return

        elif root.left is None and node.val < root.val:
            root.left = self.helper(root.left, node)
            return
        elif root.right is None and node.val > root.val:
            root.right = self.helper(root.right, node)
            return
        
        else:
            if node.val > root.val:
                self.helper(root.right, node)
            else:
                self.helper(root.left, node)
    


        
        

