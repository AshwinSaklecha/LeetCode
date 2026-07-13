class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for my_num in range(1, 10):
            digit = my_num
            curr_num = digit
            while digit < 10 and curr_num <= high:
                if curr_num <= high and curr_num >= low:
                    ans.append(curr_num)
                digit += 1
                curr_num = (curr_num*10) + digit
        
        ans.sort()
        return ans