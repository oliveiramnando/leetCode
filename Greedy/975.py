
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prevChange = 0

        currMax = maxSize = 1
        for i in range(1, len(arr)):
            change = arr[i-1] - arr[i] 
            
            if change == 0:
                currMax = 1
            elif ((prevChange < 0 and change > 0) or (prevChange > 0 and change < 0)):
                currMax += 1 
            else:
                currMax = 2
                
            maxSize = max(maxSize, currMax)
            prevChange = change
        
        return maxSize
