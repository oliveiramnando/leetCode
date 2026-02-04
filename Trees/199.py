# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can bfs and get the last node added at each level
        order = []
        if root is None:
            return order
        
        q = deque()
        q.append(root)

        while q:
            levels = []
            for _ in range(len(q)):
                node = q.popleft()
                levels.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            order.append(levels[len(levels)- 1])
        
        return order
