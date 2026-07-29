class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collides(x, y):
            if ((x < 0) and (y > 0)):
                return True
            return False
        
        res = []

        for a in asteroids:
            while res and collides(a, res[-1]) and abs(a) > abs(res[-1]):
                res.pop()

            if res and collides(a, res[-1]) and abs(a) == abs(res[-1]):
                res.pop()
                continue

            if not res or not collides(a, res[-1]):
                res.append(a)
     
        return res


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
    
            if a:
                stack.append(a)

        return stack
