class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        track = set(nums)

        r = 1
        while r < len(nums) and nums[r-1]+1 == nums[r]:
            r += 1
        
        sumLSP = sum(nums[:r])

        i = sumLSP
        while i in track:
            i += 1

        return i

