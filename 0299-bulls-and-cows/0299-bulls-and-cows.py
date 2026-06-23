class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s1 = {}
        g1 = {}
        for char in secret:
            if char in s1:
                s1[char] += 1
            else:
                s1[char] = 1
        for char in guess:
            if char in g1:
                g1[char] += 1
            else:
                g1[char] = 1
        cows = 0
        bulls = 0
        for key in g1:
            if key in s1:
                cows += min(g1[key], s1[key])
        for i in range(min(len(secret), len(guess))):
            if secret[i] == guess[i]:
                cows -= 1
                bulls += 1
        return f"{bulls}A{cows}B"