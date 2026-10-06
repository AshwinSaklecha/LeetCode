class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        ans = 0
        for char in s :
            if char == "(":
                count += 1
            else :
                count -= 1
                if count < 0 :
                    ans += (abs(count))
                    count = 0
        
        return ans + count