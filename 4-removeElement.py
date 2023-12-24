class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # This solution has a time complexity of O(n).
        nums[:] = [num for num in nums if num != val]
        return len(nums)