# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])
            
                return root
            
        return build(preorder, inorder)


# preorder = [3,9,20,15,7]
# - shows what the root is

# inorder = [9,3,15,20,7]
# - shows left and right subtrees of each node

# 1. we can take the root from preorder, look for that node in inorder
# 2. we can 'split' the array into 2 parts, the nodes on the left side of the root, and the right side, "removing the root" from both 
