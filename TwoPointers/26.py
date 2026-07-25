class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = list(set(nums))
        s.sort()
        i = 0
        while i < len(s):
            nums[i] = s[i]
            i += 1
                
        return len(s)


