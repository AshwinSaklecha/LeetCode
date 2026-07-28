class Solution:
    def smallestPalindrome(self, s: str) -> str:
        char_list = list(s)
        char_list.sort()
        ans = [None] * len(s)
        i = 0
        mid = len(ans) // 2
        idx = 0
        while idx < len(s):
            if idx + 1 < len(s) and char_list[idx] == char_list[idx+1]:
                ans[i] = char_list[idx]
                ans[len(s) - i - 1] = char_list[idx]
                i += 1
                idx += 2
            else:
                ans[mid] = char_list[idx]
                idx += 1
        return "".join(ans)