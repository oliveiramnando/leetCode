#class Solution:
#    def maxProduct(self, nums: List[int]) -> int:
#        maxProd = float('-inf')
#
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                prod = (nums[i]-1) * (nums[j]-1)
#                maxProd = max(maxProd, prod)
#        
#        return maxProd

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x, y = 0, 0 # x for the abs max, and y for the second largest value

        for n in nums:
            if n > x:         # if larger than current largest val
                y, x = x, n   # move current largest val to second spot, update largest val
            else:
                y = max(y, n)

        return (x-1) * (y-1)
