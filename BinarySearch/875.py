class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        minSpeed = 1
        maxSpeed = max(piles)
        
        k = maxSpeed
        while minSpeed <= maxSpeed:
            mid = minSpeed + (maxSpeed - minSpeed) // 2
            
            if self.canFinish(piles, h, mid):
                k = mid
                maxSpeed = mid - 1
            else:
                minSpeed = mid + 1
        
        return k
    

    def canFinish(self, piles, h, speed):
        hrs = 0 
        for p in piles:
            hrs += p // speed
            if p % speed != 0:
                hrs += 1
            if hrs > h:
                return False
        return True
        
        
