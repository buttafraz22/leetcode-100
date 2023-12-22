class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for letter in s:
            if letter not in hashmap.keys():
                hashmap[letter] = 0
            else:
                hashmap[letter] += 1
        
        for checked in t:
            if checked not in hashmap.keys():
                return False

            if hashmap[checked] == 0:
                del hashmap[checked]
            elif hashmap[checked]:
                hashmap[checked] -= 1
        
        return not hashmap
