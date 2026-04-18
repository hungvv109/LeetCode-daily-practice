class Solution:
    def intersection(self, nums1, nums2):
        return list(set(a) & set(b))