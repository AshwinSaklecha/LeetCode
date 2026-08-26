# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None :
            return head
        ans = self.reverse(None, head)
        return ans
    
    def reverse(self, prev_node, node):
        while node != None :
            next_node = node.next 
            node.next = prev_node 
            prev_node = node 
            node = next_node
        return prev_node