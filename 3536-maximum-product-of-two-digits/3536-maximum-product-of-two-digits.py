class Solution:
    def maxProduct(self, n: int) -> int:
        num1 = 0 
        num2 = 0
        while n > 0 :
            digit = n % 10 
            if digit >= num1 :
                num1, num2 = digit, num1
            else:
                num2 = max(num2, digit)
            n = n // 10
        return num1 * num2