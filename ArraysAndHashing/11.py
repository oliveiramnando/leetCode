class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        width = len(height) - 1
        max_area = float('-inf')

        while l < r:
            area = min(height[l], height[r]) * width

            if area > max_area:
                max_area = area
            
            if height[l] > height[r]:
                r -= 1
                width -= 1
                continue
            if height[l] < height[r]:
                l += 1
                width -= 1
                continue
            
            r -= 1
            width -= 1
    
        return max_area





        
