class Solution:
    def sumGame(self, num: str) -> bool:
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0
        for i in range(len(num)):
            if num[i] == "?":
                if i < len(num) // 2 :
                    left_q += 1
                else:
                    right_q += 1
                continue
            if i < len(num) // 2 :
                left_sum += int(num[i])
            else:
                right_sum += int(num[i])
        if left_sum >= right_sum :
            left_sum -= right_sum
            right_sum = 0
        else:
            right_sum -= left_sum 
            left_sum = 0
        
        if (left_q + right_q) % 2 != 0:
            return True

        return (2 * right_sum) + (9 * right_q) != (2 * left_sum) + (9 * left_q)