class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n) time complexity.
        
        length = len(nums)
        output = [0] * length

        for i in range(length):
            new_pos = (i + k) % length   # mathematical function to check new bounds
            output[new_pos] = nums[i]
        
        nums[:] = output
        return nums