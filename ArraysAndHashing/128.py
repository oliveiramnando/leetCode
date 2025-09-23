class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            #check if start of sequence
            if (n-1) not in numSet:
                length = 0 # start of sequence
                while (n + length) in numSet: 
                    length += 1 # check if nums in the set for consecutivness
                longest = max(length, longest)
        
        return longest
