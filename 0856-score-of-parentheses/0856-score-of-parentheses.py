class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []
        for char in s :
            if char == "(":
                stack.append(char)
            else:
                curr_score = 1
                if isinstance(stack[-1], int):
                    curr_score = stack.pop()
                    curr_score = curr_score * 2
                stack.pop()
                back_scores = 0
                while stack and isinstance(stack[-1], int):
                    back_scores += stack.pop()
                curr_score += back_scores
                stack.append(curr_score)
        return stack[-1]
        