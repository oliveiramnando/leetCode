class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
 
        if k >= n:
            k = k % n

        if k == 0:
            return nums

        nums.reverse()

        firstK = nums[:k]
        rest = nums[k:]

        firstK.reverse()
        rest.reverse()

        for i in range(k):
            nums[i] = firstK[i]
        
        for i in range(k,n):
            nums[i] = rest[i-k]
