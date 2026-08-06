class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, 201):
            my_num = num
            product = 1
            while my_num > 0:
                digit = my_num % 10 
                product *= digit 
                my_num = my_num // 10
            if product % t == 0:
                return num