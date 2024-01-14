class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        for char in magazine:
            if char not in hashmap.keys():
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        print(hashmap)
        for ransom in ransomNote:
            if ransom not in hashmap.keys():
                return False
            if hashmap[ransom] > 1:
                hashmap[ransom] -= 1
            elif hashmap[ransom] == 1:
                del hashmap[ransom]
            
        
        return True
