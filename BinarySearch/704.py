class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums: List[int], target: int, low: int, high: int) -> int:

        if low > high:
            return -1

        mid = (low + high) // 2

        if target < nums[mid]:
            return self.binarySearch(nums, target, low, mid-1)
        elif target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, target, mid+1, high)
            
