class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: 
            return nums
        
        l = len(nums)
        nums1 = nums[:l//2]
        nums2 = nums[l//2:l]

        arr1 = self.sortArray(nums1)
        arr2 = self.sortArray(nums2)
        arr =  self.merge(arr1,arr2)

        return arr
        
        
    
    def merge(self, arr1, arr2):        
        arr = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr.append(arr1[i])
                i += 1
                continue
            else:
                arr.append(arr2[j])
                j += 1
                continue
        
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
        

        return arr

