class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return max(self.robHelp(nums[:-1]), self.robHelp(nums[1:]))

    def robHelp(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))

        return dp[-1]
