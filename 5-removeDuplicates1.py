# code to remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This code has a complexity of O(n).
        
        # nums[:] means inplace operations.
        nums[:] = list(set(nums))
        nums[:] = sorted(nums)
        return len(nums)