# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l = 1 
        r = length-2

        # find peak
        while l <= r:
            m = l + (r-l)//2
            midL, mid, midR = mountainArr.get(m-1), mountainArr.get(m),  mountainArr.get(m+1)
            if midL < mid < midR:
                l = m + 1
            elif midL > mid > midR:
                r = m - 1
            else:
                break
        
        peak = m    # index

        # bst ascending side
        l = 0 
        r = peak
        while l <= r:
            m = l + (r-l)//2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            if target > mid:
                l = m + 1
            else:
                r = m - 1
            
        # bst descending side
        l = peak+1
        r = length-1
        while l <= r:
            m = l + (r-l)//2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            if target > mid:
                r = m - 1
            else:
                l = m + 1
        
        return -1

        
