class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(len(s)) :
            char = s[i]
            num = 27 - (ord(char) - 97 + 1) 
            print(num, num * (i+1))
            sum += (num * (i+1))
        return sum
        