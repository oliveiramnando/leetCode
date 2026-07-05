class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colores = [0,0,0] # first index for 0s, then 1s, then 2s

        for n in nums:
            if n == 0:
                colores[0] += 1
            elif n == 1:
                colores[1] += 1
            else: 
                colores[2] += 1
            
        i = 0
        while colores[0] > 0:
            nums[i] = 0
            i += 1
            colores[0] -= 1
        
        while colores[1] > 0:
            nums[i] = 1
            i += 1
            colores[1] -= 1
        
        while colores[2] > 0:
            nums[i] = 2
            i += 1
            colores[2] -= 1
