class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lower = max(nums)
        upper = sum(nums)
        res = upper

        def canSplit(x):
            curr = x
            subArrays = 1
            for n in nums:
                if curr - n < 0:
                    subArrays += 1
                    curr = x
                curr -= n 
            return subArrays <= k

        while lower <= upper:
            mid = lower + (upper-lower)//2
            
            if canSplit(mid):
                res = min(res, mid)
                upper = mid - 1
            else:
                lower = mid + 1
            

        return res
