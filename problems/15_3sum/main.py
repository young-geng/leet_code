# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []

        out = []
        nums.sort()

        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                j = i+1
                k = len(nums) - 1

                while j < k:
                    # target reached
                    if nums[i] + nums[j] + nums[k] == 0:
                        # append to output
                        out.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1

                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
        return out
