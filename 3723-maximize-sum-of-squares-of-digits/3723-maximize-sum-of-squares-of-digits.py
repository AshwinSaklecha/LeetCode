class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum :
            return ""
        nines = int(sum // 9)
        remainder = sum % 9
        zeros_remaining = num - nines - 1 if remainder != 0 else num - nines

        print(zeros_remaining)
        ans = ""
        if remainder != 0:
            ans = ("9" * nines) + str(remainder) + ("0" * zeros_remaining)
        else:
            ans = ("9" * nines) + ("0" * zeros_remaining)
        return ans