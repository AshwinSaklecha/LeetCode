class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        ans = 0
        idx = 0
        printing = []
        while idx < len(s):
            if s[idx] == ")":
                count -= 0.5
                if count < 0 :
                    if idx + 1 < len(s) and s[idx + 1] == ")":
                        ans += 1
                        idx += 2
                    else :
                        ans += 2
                        idx += 1
                    count = 0
                    continue
            else :

                count += 1
                if count % 1 != 0 :
                    ans += 1
                    count -= 0.5


            idx += 1
        ans += int(count * 2)
        return ans