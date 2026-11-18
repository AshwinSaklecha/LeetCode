class Solution:
    def minChanges(self, s: str) -> int:
        curr_count = 0
        curr_num = s[0]
        ans = 0
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char == curr_num :
                curr_count += 1
                idx += 1
            else :
                if curr_count % 2 != 0 :
                    ans += 1
                    idx += 1
                    if idx < len(s):
                        curr_num = s[idx]
                    curr_count = 0
                else :
                    curr_num = s[idx]
                    idx += 1
                    curr_count = 1
        return ans