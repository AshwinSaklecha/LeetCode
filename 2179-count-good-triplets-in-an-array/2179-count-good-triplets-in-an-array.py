class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        we could solve it using an n cube solution, but constraints are too high. 
        another approach that comes to mind is that we need to find the counts. with triplets we could do something like this - 
        we can find common elements before the element and can automatically find the remaining common elements after that element 
        just add the multiplication of common elements on both sides. repeat this for each element 
        question arises - how do we calculate the common elements and that too in less than order N ? 
        using segment trees . HOW ? 
        we keep on updating the segment tree holding the info if its visited . segment tree will be made on the nodes of array 2 

        """
        my_dict = {}
        for i in range(len(nums2)):
            my_dict[nums2[i]] = i
        seg_tree = [0] * (4 * len(nums2))

        ans = 0
        for i in range(len(nums1)):
            end_idx = my_dict[nums1[i]]
            self.update(0, 0, len(nums2)-1, end_idx, seg_tree)
            if i == 0 or i == len(nums1)-1 :
                continue
            left_common_elements = self.query(0, end_idx-1, 0, 0, len(nums2)-1, seg_tree, nums2)
            left_uncommon_elements = i - left_common_elements
            right_common_elements = len(nums2) - end_idx -1 -left_uncommon_elements
            ans += (left_common_elements * right_common_elements)
        return ans
    def query(self, start, end, seg_idx, left_idx, right_idx, seg_tree, nums2):
        if right_idx < start or left_idx > end:
            return 0
        if left_idx >= start and right_idx <= end:
            return seg_tree[seg_idx]
        mid = (left_idx + right_idx) // 2
        return self.query(start, end, 2*seg_idx + 1, left_idx, mid, seg_tree, nums2) + self.query(start, end, 2*seg_idx + 2, mid+1, right_idx, seg_tree, nums2)
    

    def update(self, seg_idx, left_idx, right_idx, target_idx, seg_tree):
        if left_idx == right_idx :
            seg_tree[seg_idx] = 1
            return 
        mid = (left_idx + right_idx) // 2 
        if target_idx <= mid :
            self.update(2*seg_idx+1, left_idx, mid, target_idx, seg_tree)
        else:
            self.update(2*seg_idx+2, mid+1, right_idx, target_idx, seg_tree)
        seg_tree[seg_idx] = seg_tree[2*seg_idx+1] + seg_tree[2*seg_idx+2]