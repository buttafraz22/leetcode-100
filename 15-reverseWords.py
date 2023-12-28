class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        s = s.split()
        
        for word in s:
            stack.append(word)
        
        stack = stack[::-1]
        return ' '.join(stack)