# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        self.traverse(root, nodes)
        nodes.sort()
        print(nodes)
        ans = self.build_tree(nodes, 0, len(nodes) - 1)
        return ans
    def build_tree(self, nodes, start, end):
        if start == end:
            return TreeNode(nodes[start])
        if end < start :
            return None
        mid = (start + end) // 2
        root = TreeNode(nodes[mid])
        root.left = self.build_tree(nodes, start, mid - 1) 
        root.right = self.build_tree(nodes, mid+1, end)
        return root 
    def traverse(self, root, nodes):
        if root == None:
            return 
        nodes.append(root.val)
        self.traverse(root.left, nodes)
        self.traverse(root.right, nodes)