class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg_tree = [None] * (4 * len(baskets))
        ans = 0
        self.build_seg_tree(0, len(baskets)-1, 0, seg_tree, baskets)
        for i in range(len(fruits)):
            greater_than_equal = fruits[i]
            gotten_idx = self.query(greater_than_equal, 0, 0, len(baskets)-1, seg_tree, baskets)
            if gotten_idx == -1:
                ans += 1
            else:
                self.update(gotten_idx, 0, 0, len(baskets) - 1, seg_tree, baskets)
        return ans
    
    def update(self, update_idx, seg_idx, left_idx, right_idx, seg_tree, baskets):
        if left_idx == right_idx :
            seg_tree[seg_idx] = -1
            return 
        mid = (left_idx + right_idx) // 2 
        if update_idx <= mid :
            self.update(update_idx, 2*seg_idx + 1, left_idx, mid, seg_tree, baskets)
        else:
            self.update(update_idx, 2*seg_idx + 2, mid+1, right_idx, seg_tree, baskets)
        
        left_node_idx = seg_tree[2*seg_idx + 1]
        right_node_idx = seg_tree[2*seg_idx + 2]
        if left_node_idx == -1 :
            seg_tree[seg_idx] = right_node_idx
        elif right_node_idx == -1 :
            seg_tree[seg_idx] = left_node_idx
        else:
            left_num = baskets[left_node_idx]
            right_num = baskets[right_node_idx]
            if left_num >= right_num :
                seg_tree[seg_idx] = left_node_idx
            else:
                seg_tree[seg_idx] = right_node_idx
        
    def query(self, gte, seg_idx, left_idx, right_idx, seg_tree, baskets):
        if seg_tree[seg_idx] == -1 or baskets[seg_tree[seg_idx]] < gte:
            return -1
        if left_idx == right_idx :
            return left_idx 
        mid = (left_idx + right_idx) // 2 
        left_node_idx = self.query(gte, 2*seg_idx + 1, left_idx, mid, seg_tree, baskets)
        if left_node_idx != -1 and baskets[left_node_idx] >= gte:
            return left_node_idx
        right_node_idx = self.query(gte, 2*seg_idx + 2, mid+1, right_idx, seg_tree, baskets)
        return right_node_idx
        

    def build_seg_tree(self, left_idx, right_idx, seg_idx, seg_tree, baskets):
        if left_idx == right_idx :
            seg_tree[seg_idx] = left_idx 
            return 
        mid = (left_idx + right_idx) // 2 
        self.build_seg_tree(left_idx, mid, 2*seg_idx + 1, seg_tree, baskets)
        self.build_seg_tree(mid+1, right_idx, 2*seg_idx + 2, seg_tree, baskets)
        left_node_idx = seg_tree[2*seg_idx + 1]
        right_node_idx = seg_tree[2*seg_idx + 2]
        left_num = baskets[left_node_idx]
        right_num = baskets[right_node_idx]
        if left_num >= right_num :
            seg_tree[seg_idx] = left_node_idx
        else:
            seg_tree[seg_idx] = right_node_idx
        