class Solution:
    def threeSumClosest(self, nums: List[int],  target: int) -> int:
        nums.sort()
        closestSum = 0 #initialize
        closest = float('inf') # intialize

        for i in range(len(nums)): 
            j = i + 1
            k = len(nums) - 1
            otherSum = target - nums[i]

            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                currCloseness = target - currSum

                if abs(currCloseness) < closest:
                    closestSum = currSum
                    closest = abs(currCloseness)

                if currCloseness > 0:
                    j += 1
                    
                else:
                    k -= 1        

        return closestSum
