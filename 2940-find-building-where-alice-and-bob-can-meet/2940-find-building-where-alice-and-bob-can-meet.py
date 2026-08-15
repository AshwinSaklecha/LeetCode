class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        seg_tree = [None] * (4 * len(heights))
        self.build_seg_tree(seg_tree, 0, 0, len(heights) -1, heights)
        ans = []
        for query in queries:
            alice_pos = min(query)
            bob_pos = max(query)
            if alice_pos == bob_pos:
                ans.append(alice_pos)
            elif heights[bob_pos] > heights[alice_pos]:
                ans.append(bob_pos)
            else:
                s = bob_pos + 1
                compare_num = max(heights[alice_pos], heights[bob_pos])
                temp_ans = self.rmiq(
                    s, compare_num,
                    0, 0, len(heights) - 1,
                    seg_tree, heights
                )
                ans.append(temp_ans)
        return ans
    def rmiq(self, s, compare_num, idx, l, r, seg_tree, heights):
        if r < s or heights[seg_tree[idx]] <= compare_num:
            return -1

        if l == r:
            return l

        mid = (l + r) // 2

        left_node_idx = self.rmiq(
            s, compare_num,
            2 * idx + 1, l, mid,
            seg_tree, heights
        )

        if left_node_idx != -1:
            return left_node_idx

        right_node_idx =  self.rmiq(
            s, compare_num,
            2 * idx + 2, mid + 1, r,
            seg_tree, heights
        )
        return right_node_idx

    def build_seg_tree(self, seg_tree, idx, l, r, heights):
        if l == r :
            seg_tree[idx] = l
            return 
        mid = (l + r) // 2 
        self.build_seg_tree(seg_tree, (2*idx)+1, l, mid, heights)
        self.build_seg_tree(seg_tree, (2*idx)+2, mid+1, r, heights)
        left_tree_idx = seg_tree[(2*idx)+1]
        right_tree_idx = seg_tree[(2*idx)+2]
        left_num = heights[left_tree_idx]
        right_num = heights[right_tree_idx]
        if left_num >= right_num:
            seg_tree[idx] = left_tree_idx
        else:
            seg_tree[idx] = right_tree_idx