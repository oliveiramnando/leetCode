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
