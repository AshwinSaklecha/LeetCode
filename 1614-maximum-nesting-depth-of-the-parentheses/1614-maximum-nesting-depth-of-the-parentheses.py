class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        ans = 0
        for char in s :
            if char == "(":
                open += 1
                ans = max(ans, open)
            elif char == ")":
                open -= 1

        return ans