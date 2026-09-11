class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        my_set = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i == j :
                    continue
                for k in range(len(digits)):
                    if k == j or k == i :
                        continue
                    digit1 = digits[i]
                    digit2 = digits[j]
                    digit3 = digits[k]
                    full_num = (((digit1 * 10 ) + digit2) * 10) + digit3
                    if digit1 != 0 and digit3 % 2 == 0 :
                        my_set.add(full_num)
        
        return len(my_set)
        