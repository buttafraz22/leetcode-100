class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # This code has a time complexity of O(n).
        
        # Create a dictionary to store the frequency of each element
        counts = {}

        # Fill the dictionary
        for i in nums:
            if i not in counts.keys():
                counts[i] = 1
            else:
                counts[i] += 1

        buffer = len(nums) // 2

        for k, v in counts.items():
            # If the count of an element is greater than the threshold, it is the majority element
            if v > buffer:
                return k