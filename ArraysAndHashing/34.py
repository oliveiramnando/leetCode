class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target: 
                l = m + 1
            else:
                res = [m,m]
                ri = m
                le = m
                while((ri <= r) and (nums[ri] == target)):
                    res[1] = ri
                    ri += 1
                
                while ((le >= l) and (nums[le] == target)):
                    res[0] = le
                    le -= 1
                return res
        return res
