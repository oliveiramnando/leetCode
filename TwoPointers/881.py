class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        n = len(people)
        l, r = 0, n-1

        res = 0

        while l <= r:
            if l == r:
                res += 1
                break

            fill = limit - people[r]

            if fill == 0:
                res += 1
                r -= 1
                continue

            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
    
        return res

        
