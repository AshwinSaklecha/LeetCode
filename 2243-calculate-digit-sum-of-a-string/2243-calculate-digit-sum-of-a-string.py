class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k :
            s = self.recursion(s, k)
        return s
    
    def recursion(self, s, k):
        str_list = list(s)
        ans_list = []
        idx = 0 
        while idx < len(str_list):
            sum = 0
            last_idx = idx + k
            while idx < last_idx and idx < len(str_list):
                sum += int(str_list[idx])
                idx += 1
            ans_list.append(str(sum))
        print(ans_list)
        final_str = "".join(ans_list)
        return final_str