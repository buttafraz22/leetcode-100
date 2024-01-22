class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_i = {}

        for i, n in enumerate(nums):
            if n in num_to_i and abs(i-num_to_i[n]) <= k:
                return True
            
            num_to_i[nums[i]] = i
        
        return False
