class Solution:
    def minSteps(self, n: int) -> int:
        ans = self.traverse(0, 1, n)
        return ans
    
    def traverse(self, copy, curr_chars, n):
        if curr_chars == n :
            return 0
        if curr_chars > n :
            return float('inf')

        path1 = 2 + self.traverse(curr_chars, curr_chars + curr_chars, n)
        path2 = float('inf')
        if copy > 0:
            path2 = 1 + self.traverse(copy, curr_chars + copy, n)

        return min(path1 ,path2)
        

        

        