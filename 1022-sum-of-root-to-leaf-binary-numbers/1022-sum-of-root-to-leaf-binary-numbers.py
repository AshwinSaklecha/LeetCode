# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse("", root)
        return self.ans 
    
    def traverse(self, curr_str, root):
        if root == None:
            return 
        if root.left == None and root.right == None:
            binary_val = self.calculate(curr_str + str(root.val))
            self.ans += binary_val
            return 
        self.traverse(curr_str + str(root.val), root.left)
        self.traverse(curr_str + str(root.val), root.right)
    
    def calculate(self, curr_str):
        curr_str = curr_str[::-1]
        two_power = 0
        ans = 0
        for char in curr_str:
            ans += int(char) * (2 ** two_power)
            two_power += 1
        return ans