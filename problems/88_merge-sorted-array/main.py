# https://leetcode.com/problems/merge-sorted-array/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while k >= 0:
            # moving from the back, check if nums1 is bigger
            if j < 0 or (i >= and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            # nums2 element is larger
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
