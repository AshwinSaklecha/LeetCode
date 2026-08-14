class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 1
        my_dict = {}
        while j < len(s):
            if s[j] in my_dict:
                my_dict[s[j]] += 1
            else:
                my_dict[s[j]] = 1
            while my_dict[s[j]] > 2:
                my_dict[s[i]] -= 1
                if my_dict[s[i]] == 0:
                    my_dict.pop(s[i])
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans