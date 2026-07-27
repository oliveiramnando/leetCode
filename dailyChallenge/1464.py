class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float('-inf')

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = (nums[i]-1) * (nums[j]-1)
                maxProd = max(maxProd, prod)
        
        return maxProd
