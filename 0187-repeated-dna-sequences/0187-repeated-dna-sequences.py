class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        i = 0
        j = 0 
        temp_str = ""
        my_dict = {}
        while j < len(s):
            if j - i + 1 < 11 :
                temp_str = temp_str + s[j]
            else :
                temp_str = temp_str[1:] + s[j]
                i += 1
                # now add in my_dict 
            if j - i + 1 == 10 :
                if temp_str in my_dict :
                    my_dict[temp_str] += 1
                else:
                    my_dict[temp_str] = 1
            j += 1
        
        ans = []
        for key in my_dict :
            if my_dict[key] > 1:
                ans.append(key)
        return ans