
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        currMax = maxSum = nums[0]
        currMin = minSum = nums[0]

        for n in nums[1:]:
            currMax = max(n, currMax + n)
            maxSum = max(maxSum, currMax)

            currMin = min(n, currMin + n)
            minSum = min(minSum, currMin)
        
        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)
