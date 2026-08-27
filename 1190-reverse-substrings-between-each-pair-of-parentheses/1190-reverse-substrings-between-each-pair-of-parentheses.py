class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s :
            if char == ")":
                temp_str_holder = []
                while stack[-1] != "(":
                    temp_str_holder.append(stack.pop())
                stack.pop()
                for new_char in temp_str_holder:
                    stack.append(new_char)
            else:
                stack.append(char)
        return "".join(stack)        