class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = int(1e9) + 7
        sum_ps = [0]
        digit_ps = [0]
        num_ps = [0]
        pow10 = [1] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            pow10[i] = (pow10[i-1] * 10) % mod

        for i in range(len(s)):
            sum_ps.append(sum_ps[-1] + int(s[i]))
            if s[i] != "0":
                digit_ps.append(digit_ps[-1] + 1)
                num_ps.append((num_ps[-1] * 10 + int(s[i])) % mod)
            else:
                digit_ps.append(digit_ps[-1])
                num_ps.append(num_ps[-1])
        ans = []
        for chunk in queries:
            s, e = chunk 
            sum = sum_ps[e+1] - sum_ps[s]
            digit_diff = digit_ps[e+1] - digit_ps[s]
            num1 = num_ps[s]
            num2 = num_ps[e+1]
            num1_subtractable = (num1 * (pow10[digit_diff])) % mod
            temp_ans = ((num2 - num1_subtractable + mod) * sum) % mod
            ans.append(temp_ans)
        return ans 