class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        my_dict = {}
        for char in word :
            if ord(char) >= 97 :
                if char in my_dict:
                    my_dict[char] += 1
                else:
                    my_dict[char] = 1
        ans = 0
        for i in range(len(word)):
            ascii_val = ord(word[i])
            if ascii_val >= 97:
                if word[i] in my_dict:
                    my_dict[word[i]] -= 1
            else:
                small_ascii_val = ascii_val + 32
                small_char = chr(small_ascii_val)
                if small_char in my_dict:
                    if my_dict[small_char] == 0:
                        ans += 1
                    my_dict.pop(small_char)
        return ans