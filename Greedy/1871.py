

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        reachable = [False] * n
        reachable[0] = True

        farthestScanned = 0

        for i in range(n):
            if not reachable[i]:
                continue
            
            l = max(i + minJump, farthestScanned + 1)
            r = min(i + maxJump, n - 1)
            
            for j in range(l, r+1):
                if s[j] == '0':
                    reachable[j] = True

            farthestScanned = max(farthestScanned, r)
        
        return reachable[-1]





