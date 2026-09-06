
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
            
        if goal == 0:
            return True
        
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
    
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            
        return True
