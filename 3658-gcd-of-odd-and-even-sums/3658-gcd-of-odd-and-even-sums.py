class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0 
        even_sum = 0
        is_odd = True
        for i in range(1, (n * 2) + 1):
            if is_odd:
                odd_sum += i
            else:
                even_sum += 1
            is_odd = not is_odd

        return math.gcd(odd_sum, even_sum)