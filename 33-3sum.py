class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        if len(nums) < 3:
            return res
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s > 0:
                    high -= 1
                elif s < 0:
                    low += 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    lastLowOccurrence, lastHighOccurrence = nums[low], nums[high]
                    
                    while low < high and nums[low] == lastLowOccurrence:
                        low += 1
                    
                    while low < high and nums[high] == lastHighOccurrence:
                        high -= 1
        
        return res
