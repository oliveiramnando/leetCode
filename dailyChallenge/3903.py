
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        smallest = k + 1
        si = -1
        for i in range(n):
            l = nums[:i+1]
            r = nums[i:]
            maxi = max(l)
            mini = min(r)
    
            instScore = maxi-mini
            
            if instScore < smallest:
                si = i
                break
          
        return si
