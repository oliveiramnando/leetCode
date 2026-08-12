class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxLen = 0
        track = {}
        l = 0

        for r in range(len(nums)):
            track[nums[r]] = track.get(nums[r], 0) + 1

            while track[nums[r]] > k:
                track[nums[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            
        return maxLen
