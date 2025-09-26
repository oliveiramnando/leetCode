class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        size = len(nums)
        if size % 3 != 0:
            return []

        nums.sort()

        result = []
        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k: # ensures there are 3 numbers starting from i; ensures difference is <= k
                result.append([nums[i], nums[i + 1], nums[i + 2]]) # adds to result
            else:
                return []
        return result
