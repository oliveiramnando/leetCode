class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        for key, value in count.items():
            if value > (len(nums)/3):
                res.append(key)
        
        return res
