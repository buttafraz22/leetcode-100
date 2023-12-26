class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time complexity: O(n).
        
        n = len(nums)
        max_reach = nums[0]
        end = nums[0]

        jump = 1
        if n == 1:
            return 0
        
        for i in range(1, n-1):
            max_reach = max(max_reach, i + nums[i])
            if i == end:
                end = max_reach

                jump += 1
        
        return jump
