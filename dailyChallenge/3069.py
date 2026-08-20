class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # if arr[-1] > arr[-1] then add to arr1. else add to arr2
        print(nums)
        arr1 = [nums.pop(0)]
        print(nums)
        arr2 = [nums.pop(0)]
        print(nums)   
        print(arr1)   
        print(arr2)  
        while nums:
            n = nums.pop(0)
            if arr1[-1] > arr2[-1]:
                arr1.append(n)
            else:
                arr2.append(n)
    
        return arr1 + arr2

        
