class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        min_removals = self.find_removals(s)
        print(min_removals)
        self.ans = set()
        self.traverse(0, 0, min_removals, "", s)
        final_ans = []
        for key in self.ans:
            final_ans.append(key)
        return final_ans
    
    def traverse(self, idx, count, min_removals, temp_ans, s):
        if min_removals < 0 or count < 0:
            return
        if idx >= len(s):
            if count == 0 and min_removals == 0:
                self.ans.add(temp_ans)
            return
        curr_char = s[idx]
        if 97 <= ord(curr_char) <= 122:
            self.traverse(idx+1, count, min_removals, temp_ans + curr_char, s)
        else:
            new_count = 0
            if curr_char == "(":
                new_count = count + 1
            elif curr_char == ")":
                new_count = count - 1
            # take 
            self.traverse(idx+1, new_count, min_removals, temp_ans + curr_char, s)
            # skip 
            self.traverse(idx+1, count, min_removals-1, temp_ans, s)
        
    
    def find_removals(self, s):
        count = 0
        ans = 0
        for char in s :
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
                if count < 0 :
                    ans += abs(count)
                    count = 0

        ans += count 
        return ans