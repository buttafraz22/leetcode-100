class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            t=''.join(sorted(word))
            if t in hashmap:
                hashmap[t].append(word)
            else:
                hashmap[t]= [word]
        

        return hashmap.values()
