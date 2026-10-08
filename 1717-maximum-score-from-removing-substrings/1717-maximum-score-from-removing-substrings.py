class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        char1 = "a"
        char2 = "b"
        ans = 0
        if x > y :
            count1, new_str = self.compute(char1, char2, x, s)
            ans += count1
            count2, new_str = self.compute(char2, char1, y, new_str)
            ans += count2
        else:
            count1, new_str = self.compute(char2, char1, y, s)
            ans += count1
            count2, new_str = self.compute(char1, char2, x, new_str)
            ans += count2
        
        return ans
    
    def compute(self, char1, char2, to_add, s):
        count = 0
        stack = []
        for char in s :
            if char == char2 :
                if stack and stack[-1] == char1 :
                    stack.pop()
                    count += to_add
                else :
                    stack.append(char)
            else :
                stack.append(char)
        
        new_str = "".join(stack)
        return count, new_str