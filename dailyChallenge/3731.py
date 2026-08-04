class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()

        p = nums[0] 
        i = 0

        while i < len(nums):
            if nums[i] != p:
                res.append(p)
            else:
                i += 1

            p += 1

        return res

