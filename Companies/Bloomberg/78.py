class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i): # is the index of the value we are making the decision on
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to inlcude nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # decison not to include; empty subset given to it
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
