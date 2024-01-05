class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = 1,1
        res = [0] * n
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res