class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        my_set1 = set()
        my_set2 = set()
        ans = [0] * len(A)
        for i in range(len(A)):
            count = 0
            if A[i] == B[i]:
                ans[i] = ans[i-1] + 1
                continue
            else:
                if A[i] in my_set2:
                    count += 1
                    my_set2.remove(A[i])
                else:
                    my_set1.add(A[i])
                if B[i] in my_set1:
                    count += 1
                    my_set1.remove(B[i])
                else:
                    my_set2.add(B[i])
            ans[i] = ans[i-1] + count
        return ans