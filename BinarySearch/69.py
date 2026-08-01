class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m

        return res


class Solution:
    def mySqrt(self, x: int) -> int:
        if x==2 or x==3:
            return 1
        
        for i in range(3, x):
            if i * i == x:
                return i
            if i*i > x:
                return i-1
        
        return x
