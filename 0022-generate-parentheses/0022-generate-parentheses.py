class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.traverse(0, 0, n, "")
        return self.ans
    
    def traverse(self, open, close, n, temp_ans):
        if close == open and open == n :
            self.ans.append(temp_ans)
            return 
        if close > open or open > n :
            return 
        path1 = self.traverse(open + 1, close, n, temp_ans + "(")
        path2 = self.traverse(open, close + 1, n, temp_ans + ")")