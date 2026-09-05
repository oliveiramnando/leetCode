

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        minSuffix = [0] * n
        minSuffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            minSuffix[i] = min(nums[i], minSuffix[i + 1])

        maxPrefix = nums[0]

        for i in range(n):
            maxPrefix = max(maxPrefix, nums[i])
            
            instaScore = maxPrefix - minSuffix[i]
            if instaScore <= k:
                return i
        
        return -1

