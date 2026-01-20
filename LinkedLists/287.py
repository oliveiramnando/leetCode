class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        track = set()
        for i in range(len(nums)):
            if nums[i] not in track:
                track.add(nums[i])
            else:
                return nums[i]
        return 
        
