class Solution:
    def checkString(self, s: str) -> bool:
        a = 0
        b = 0
        for char in s :
            if char == "a":
                if b > 0 :
                    return False
                a += 1
            else :
                b += 1
        return True