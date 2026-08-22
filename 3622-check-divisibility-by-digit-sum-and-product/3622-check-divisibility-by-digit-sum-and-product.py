class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1 
        num = n 
        while num > 0 : 
            digit = num % 10 
            sum += digit 
            product *= digit
            num = num // 10 
        print(sum, product)
        return n % (product + sum) == 0 
        