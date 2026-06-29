class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for chunk in patterns :
            if chunk in word:
                ans += 1
        return ans