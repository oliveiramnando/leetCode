class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: #keep track of product alr 
        res = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                copy = nums[:i] + nums[i+1:]
                prod = self.prodList(copy)
                res.append(prod)
                continue
            prodExcept = product // nums[i]
            res.append(prodExcept)
        
        return res

    def prodList(self, nums: list[int]) -> int:
        res = 1
        for i in range(len(nums)):
            res *= nums[i]
        return res

