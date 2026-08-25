

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = k
        for n in nums:
            if n == res:
                res += k 

        return res
