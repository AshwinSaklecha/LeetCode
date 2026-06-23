class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        ans = self.solve(r, k) - self.solve(l-1, k)
        return ans
    def solve(self, num, diff):
        self.dp = [[[[None] * 16 for _ in range(2)] for _ in range(2)] for _ in range(11)]
        num_str = str(num)
        ans = self.traverse(0, True, True, -1, diff, num_str)
        return ans
    def traverse(self, idx, is_leading_zero, is_tight, prev_num, diff, num_str):
        if idx >= len(num_str): # not sure about this case
            return 1 # going to be wrong for cases like 00001, 001, etc
        is_leading_zero_idx = 0 if is_leading_zero else 1
        is_tight_idx = 0 if is_tight else 1
        if self.dp[prev_num][is_tight_idx][is_leading_zero_idx][idx] != None:
            return self.dp[prev_num][is_tight_idx][is_leading_zero_idx][idx]
        last_num = int(num_str[idx]) if is_tight else 9
        ans = 0
        for num in range(0, last_num + 1):
            if (prev_num != -1 and abs(num - prev_num) <= diff) or is_leading_zero:
                new_is_leading_zero = is_leading_zero and num == 0
                new_prev_num = -1 if new_is_leading_zero else num
                new_is_tight = is_tight and num == last_num
                ans += self.traverse(idx + 1, new_is_leading_zero,new_is_tight, new_prev_num, diff, num_str)
        self.dp[prev_num][is_tight_idx][is_leading_zero_idx][idx] = ans
        return self.dp[prev_num][is_tight_idx][is_leading_zero_idx][idx]