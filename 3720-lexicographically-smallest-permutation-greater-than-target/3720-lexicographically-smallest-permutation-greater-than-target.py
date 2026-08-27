class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        my_dict = {}
        my_set = SortedSet()
        for char in s :
            if char in my_dict :
                my_dict[char] += 1
            else:
                my_dict[char] = 1
                my_set.add(char)

        ans = []

        ready_to_go_back = False 
        ready_to_insert = False

        idx = 0 
        while idx < len(s):
            needed_char = target[idx]
            if needed_char in my_dict :
                my_dict[needed_char] -= 1 
                ans.append(needed_char)
                if my_dict[needed_char] == 0 :
                    my_dict.pop(needed_char)
                    my_set.remove(needed_char)
            else:
                if ord(my_set[-1]) > ord(needed_char):
                    ready_to_insert = True
                    break
                else :
                    ready_to_go_back = True 
                    break
            idx += 1
        
        if len(ans) == len(s):
            ready_to_go_back = True
        
        if ready_to_go_back :
            while len(ans) > 0 :
                idx -= 1
                popped = ans.pop()
                my_set.add(popped)
                if popped in my_dict :
                    my_dict[popped] += 1
                else :
                    my_dict[popped] = 1
                
                # check from here 
                if ord(my_set[-1]) > ord(target[idx]):
                    ready_to_insert = True
                    break

        if ready_to_insert : 
            # step 1 : find the element just greater , its sure to be present there
            greater_idx = my_set.bisect_right(target[idx])
            if greater_idx >= len(my_set):
                return ""
            greater_char = my_set[greater_idx]
            my_dict[greater_char] -= 1
            ans.append(greater_char)

            # now keep on appending the chars from starting 

            for char in my_set :
                while my_dict[char] > 0:
                    ans.append(char)
                    my_dict[char] -= 1
        final_ans = "".join(ans)
        return final_ans