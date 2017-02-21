# https://leetcode.com/problems/find-peak-element/
"""
         5   5                           5
        / \ / \                         / \
       4   4   4                       4  -∞
      /         \                     /
     3           3           3       3
    /             \         / \     /
   2               2       2   2   2
  /                 \     /     \ /
-∞                   1   1       1
                      \ /
                       0
   0 1 2 3 4 5 6 7 8 910111213141516171819 indices
   2,3,4,5,4,5,4,3,2,1,0,1,2,3,2,1,2,3,4,5 (20 nums)
   l                 m                   r l=0, m=9, r=19
   l       m         r                     l=0, m=4, r= 9
             l   m   r                     l=5, m=7, r= 9
             l>m r                         l=5, m=6, r= 7
  return n[l] > n[l + 1])? l : r

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            midi = left + (right - left) / 2
            if nums[midi] < nums[midi+1]:
                left = midi + 1
            else:
                right = midi
        return left
