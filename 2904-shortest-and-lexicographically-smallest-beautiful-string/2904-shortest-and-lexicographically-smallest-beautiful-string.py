class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0 
        j = 0 
        count = 0
        ans = s
        while j < len(s):
            if s[j] == "1":
                count += 1
            while count >= k :
                # if len(ans) >= j - i + 1:
                if int(ans, 2) >= int(s[i:j+1], 2):
                    ans = s[i:j+1]
                if s[i] == "1":
                    count -= 1
                i += 1
            j += 1
        # need postcheck 
        count_of_ones = 0
        for char in ans :
            if char == "1":
                count_of_ones += 1
        if count_of_ones < k :
            return ""
        return ans