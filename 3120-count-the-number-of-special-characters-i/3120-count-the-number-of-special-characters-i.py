class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        my_set = set()
        for char in word :
            if ord(char) >= 97:
                my_set.add(char)
        # set contains all small elements 
        print(my_set)
        for char in word:
            if ord(char) < 97:
                new_char = chr(ord(char) + 32)
                print(new_char)
                if new_char in my_set:
                    ans += 1
                    my_set.remove(new_char)
        return ans