class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) == 1:
            return 0
        zero_left_to_right = [0]
        one_left_to_right = [0]
        zero_right_to_left = [0]
        one_right_to_left = [0]
        for i in range(1, len(s)):
            if s[i-1] == "0":
                zero_left_to_right.append(zero_left_to_right[-1] + 1)
                one_left_to_right.append(one_left_to_right[-1])
            else:
                one_left_to_right.append(one_left_to_right[-1] + 1)
                zero_left_to_right.append(zero_left_to_right[-1])
        for i in range(len(s)-1-1, -1, -1):
            if s[i+1] == "0":
                zero_right_to_left.append(zero_right_to_left[-1] + 1)
                one_right_to_left.append(one_right_to_left[-1])
            else:
                one_right_to_left.append(one_right_to_left[-1] + 1)
                zero_right_to_left.append(zero_right_to_left[-1])
        one_right_to_left.reverse()
        zero_right_to_left.reverse()
        ans = float('inf')
        # all 4 lists made, now do the operations 
        for i in range(len(s)):
            # case 1, convert left to zeros and right to ones 
            new_ans = one_left_to_right[i] + zero_right_to_left[i]
            ans = min(ans, new_ans)
            # case 2, convert zero on both sides 
            new_ans = one_left_to_right[i] + one_right_to_left[i]
            if s[i] == "1":
                new_ans += 1
            ans = min(ans, new_ans)
            # case 3, convert one on both sides
            new_ans = zero_left_to_right[i] + zero_right_to_left[i]
            if s[i] == "0":
                new_ans += 1
            ans = min(ans, new_ans)
        return ans