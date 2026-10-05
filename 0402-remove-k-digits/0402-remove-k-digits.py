class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num :
            while stack and int(stack[-1]) > int(char) and k > 0:
                stack.pop()
                k -= 1
            stack.append(char)
        
        while k > 0 and stack :
            stack.pop()
            k -= 1
        
        stack.reverse()
        while stack and stack[-1] == "0":
            stack.pop()
        stack.reverse()
        ans = "".join(stack)
        return ans if len(ans) >= 1 else "0"
