
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def average(root):
            if not root:
                return 0, 0
            nonlocal res 

            l, totalL = average(root.left)
            r, totalR = average(root.right)

            total = root.val + totalL + totalR
            currAverage = total // (l + r + 1)

            if currAverage == root.val:
                res += 1

            return [l + r + 1, total]

        average(root)
        return res


