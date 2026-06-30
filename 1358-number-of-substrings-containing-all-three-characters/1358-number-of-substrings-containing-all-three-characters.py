class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        my_dict = {}
        while j < len(s):
            # logic 
            # first add the element 
            # then keep on removing until my_dict length is 3, and also keep on adding the number substrings in ans
            if s[j] in my_dict:
                my_dict[s[j]] += 1
            else:
                my_dict[s[j]] = 1
            
            while len(my_dict) == 3:
                ans += len(s) - j
                my_dict[s[i]] -= 1
                if my_dict[s[i]] == 0:
                    my_dict.pop(s[i])
                i += 1
            j += 1
        return ans