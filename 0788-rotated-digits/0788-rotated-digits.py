class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for num in range(1, n+1):
            if self.is_good(num):
                ans += 1
        return ans
    def is_good(self, num):
        store = num
        print(store)
        rotated = 0
        factor = 1
        while store > 0:
            digit = store % 10
            if digit == 3 or digit == 4 or digit == 7:
                return False
            elif digit == 2 :
                digit = 5 
            elif digit == 5 :
                digit = 2 
            elif digit == 6 :
                digit = 9
            elif digit == 9 :
                digit = 6
            rotated = (digit * factor ) + rotated 
            factor *= 10
            store //= 10
        return True if rotated != num else False