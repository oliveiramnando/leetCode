class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # checks if the current elemnt is a duplicate of previous 
                continue                       # skips if it is, Handles duplicate lists
            target = -(nums[i])
            j = i + 1
            k = len(nums) - 1
            while j < k:    # two sum approcah
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1      # handles duplicate triplets
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

                if nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res



