class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time complexity. Two pointer approach.
        
        res = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0


        while left < right:
            if height[left] < height[right]:

                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
                left += 1
            
            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                right -= 1
        
        return res

        