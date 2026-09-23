# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float('-inf')
        self.traverse(root)
        return self.ans
    
    def traverse(self, root):
        if root == None:
            return 0
        left_max_path_sum = max(0, self.traverse(root.left))
        right_max_path_sum = max(0, self.traverse(root.right))
        self.ans = max(self.ans, root.val + left_max_path_sum + right_max_path_sum)
        return root.val + max(left_max_path_sum, right_max_path_sum)