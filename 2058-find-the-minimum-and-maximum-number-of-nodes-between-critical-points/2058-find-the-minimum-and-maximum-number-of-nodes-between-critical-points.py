# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        last_critical_node = None
        min_dist = float('inf')
        max_dist = float('-inf')

        min_curr_dist = 0
        max_curr_dist = 0

        ptr = head.next
        last_ptr = head

        while ptr != None and ptr.next != None:
            if (ptr.val > last_ptr.val and ptr.val > ptr.next.val) or (ptr.val < last_ptr.val and ptr.val < ptr.next.val):
                if last_critical_node :
                    min_dist = min(min_dist, min_curr_dist)
                    min_curr_dist = 0
                    max_dist = max_curr_dist
                last_critical_node = ptr
            if last_critical_node != None:
                max_curr_dist += 1
                min_curr_dist += 1
            ptr, last_ptr = ptr.next, ptr
        
        if min_dist == float('inf'):
            return [-1, -1]
        return [min_dist, max_dist]
            



        