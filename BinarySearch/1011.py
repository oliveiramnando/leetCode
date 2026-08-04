class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = max(weights)
        upper = sum(weights)
        res = upper

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w

            return ships <= days

        while lower <= upper:
            capacity = (lower + upper) // 2
            if canShip(capacity):
                res = min(res, capacity)
                upper = capacity - 1
            else:
                lower = capacity + 1

        return res


