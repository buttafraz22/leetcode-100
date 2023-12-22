class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This solution has a time complexity of O(n).
        
        hashmap = {}

        for letter in s:
            # Create a counters dictionary of letters from the first string
            if letter not in hashmap.keys():
                hashmap[letter] = 0
            else:
                hashmap[letter] += 1
        
        for checked in t:

            # EDGE CASE: if dictionary of first word's characters is empty
            # and the second word still contains letters, it cant be anagrams
            if checked not in hashmap.keys():
                return False
            
            # deduct occurences of each letter from second character from the
            # first letter's dictionary.
            # If it is zero, then remove the occurence, else -1.
            if hashmap[checked] == 0:
                del hashmap[checked]
            elif hashmap[checked]:
                hashmap[checked] -= 1
        

        # If the two strings are anagrams, then this hashmap variable should be
        # empty at the end.
        return not hashmap