class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This code has a time complexity of O(n).
        
        # Two pointers, l (left) and r (right), iterate through the array
        l, r = 0, 0

        # Main loop: keep moving the right pointer until we find a different number
        while r < len(nums):
            count = 1

            # Inner loop: if we find the same number, move the right pointer further until we find a different number
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            
            # If the count is 1 or 2, move the left pointer and copy the current number into the left pointer position
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            
            # Move the right pointer further
            r += 1
        
        # Return the new length of the array
        return l
        