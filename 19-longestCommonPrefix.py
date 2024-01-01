class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # The idea is that we are using some brainstorming. We are sorting the 
        # input list, and then only considering the first and last elements of 
        # this sorted list. In this way, we only have to compare the first and last
        # elements (two) of the array to find the longest common prefix.
        
        # A downside of this algorithm is that it runs in a O(m + m logm) time. The
        # mlogm time overhead is due to sorting the input list. 
        ret=""
        strs = sorted(strs)
        first=strs[0]
        last=strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ret
            
            ret += first[i]    # or last[i]
        
        return ret
        