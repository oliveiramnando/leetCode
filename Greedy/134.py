
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        total = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                tank = 0
                start = i + 1
        
        if total < 0:
            return -1

        return start



class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gasLeft = []
        for i in range(n):
            g = gas[i] - cost[i]
            gasLeft.append(g)
        
        gl = sum(gasLeft)

        if gl < 0:
            return -1
        
        gasTank = 0
        start = 0
        for i in range(n):
            gasTank += gasLeft[i]
            if gasTank < 0:
                gasTank = 0
                start = i + 1
            
        return start
