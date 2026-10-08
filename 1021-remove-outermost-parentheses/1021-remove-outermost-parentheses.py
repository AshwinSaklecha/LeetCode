class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 1 
        idx = 1
        stack = []
        while idx < len(s):
            if s[idx] == "(":
                count += 1
            else :
                count -= 1
            if count == 0 :
                idx += 2
                count = 1
                continue
            stack.append(s[idx])
            idx += 1

        ans = "".join(stack)
        return ans