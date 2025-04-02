class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        sumOfNums = 0
        left = 0

        for right in range(len(nums)):
            sumOfNums += nums[right]

            #check if its equal to target, if it is update length
            if sumOfNums >= target:
                min_len = min(min_len, right - left + 1)

            while sumOfNums > target: # constrict window
                sumOfNums -= nums[left]
                left += 1
                if sumOfNums < target:
                    left -= 1
                    sumOfNums += nums[left]
                    min_len = min(min_len, right - left + 1)
                    break
            
            #check if its equal to target, if it is update length
            if sumOfNums >= target:
                min_len = min(min_len, right - left + 1)

        if sumOfNums < target:
            return 0

        return min_len

# ---------- Optimization ---------- #
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float("inf") else 0
