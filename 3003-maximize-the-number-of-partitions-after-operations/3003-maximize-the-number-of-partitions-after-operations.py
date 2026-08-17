class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        self.dp = {}
        ans = self.traverse(0, 0, True, s, k)
        return ans
    
    def traverse(self, idx, visited_chars, can_change, s, k):
        if idx >= len(s):
            return 1
        can_change_idx = 0 if can_change else 1
        if (can_change_idx, visited_chars, idx) in self.dp:
            return self.dp[(can_change_idx, visited_chars, idx)]
        char_idx = ord(s[idx]) - ord('a')
        ans = 0

        # case 1 
        if can_change : 
            temp_ans = 0
            for i in range(0, 26):
                new_visited_chars = visited_chars | (1 << i)
                set_bits = new_visited_chars.bit_count()
                if set_bits > k :
                    to_be_sent_chars = 1 << i
                    temp_ans = 1 + self.traverse(idx + 1, to_be_sent_chars, False, s, k)
                else:
                    temp_ans = self.traverse(idx + 1, new_visited_chars, False, s, k)
                ans = max(ans, temp_ans)

        # case 2 when we just dont wanna change 
        new_visited_chars = visited_chars | (1 << char_idx)
        set_bits = new_visited_chars.bit_count()
        if set_bits > k :
            to_be_sent_chars = 1 << char_idx
            ans = max(ans, 1 + self.traverse(idx + 1, to_be_sent_chars, can_change, s, k))
        else:
            ans = max(ans, self.traverse(idx+1, new_visited_chars, can_change, s, k))
        self.dp[(can_change_idx, visited_chars, idx)] = ans
        return self.dp[(can_change_idx, visited_chars, idx)]