class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            if n not in d:
                d[n] = 0
            
            d[n] += 1
        
        return max(d, key=d.get)

        
