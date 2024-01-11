class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        idx, step = 0, -1
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        return ''.join(rows)