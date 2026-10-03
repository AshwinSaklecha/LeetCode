class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        for char in s :
            if char == "(":
                stack.append(char)
            else :
                store = 0
                if stack and isinstance(stack[-1], int):
                    store = stack.pop()
                flag = False
                if stack and stack[-1] == "(":
                    flag = True
                    stack.pop()
                if flag :
                    total_val = store + 2
                    # now also add with previous elements too 
                    while stack and isinstance(stack[-1], int):
                        total_val += stack.pop()
                    stack.append(total_val)
                    ans = max(ans, total_val) 
                else :
                    if store != 0 :
                        stack.append(store)
                    stack.append(char)
        return ans