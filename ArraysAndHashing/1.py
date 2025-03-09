class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i 

        
