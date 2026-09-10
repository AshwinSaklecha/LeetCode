# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        self.traverse(root)
        return self.ans
    
    def traverse(self, root):
        if root == None :
            return [0, 0]
        
        freq_sum = [1, root.val]
        left_freq_sum = self.traverse(root.left)
        right_freq_sum = self.traverse(root.right)

        total_freqs = 1 + left_freq_sum[0] + right_freq_sum[0]
        total_sum = root.val + left_freq_sum[1] + right_freq_sum[1]
        avg = (total_sum // total_freqs)
        if avg == root.val:
            self.ans += 1 

        freq_sum[0] = total_freqs
        freq_sum[1] = total_sum

        return freq_sum