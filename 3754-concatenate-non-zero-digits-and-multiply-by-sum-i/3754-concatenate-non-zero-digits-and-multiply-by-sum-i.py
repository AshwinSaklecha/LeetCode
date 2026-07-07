class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        num = 0
        multiplier = 1
        while n > 0 :
            digit = n % 10 
            if digit > 0:
                num = (digit * multiplier) + num 
                multiplier *= 10
            sum += digit
            n = n // 10
        
        return num * sum
        