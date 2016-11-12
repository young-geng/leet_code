# https://leetcode.com/problems/missing-ranges/

# Algorithm:
# Move throught the nums array. For each point indicate what is the missing range.

# We will keep a marker pointing to the lowest missing range at first
# and we will keep updating this marker pointer to add missing ranges. This
# is equivalent as thinking it as a number line and just grabbing chunks of
# missing ranges as we move from the array of numbers available to us.

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        # at first marker points to the lower end of range
        marker = lower
        for i in xrange(len(nums)):
            # we dont care about the numbers that are below our lower point
            if nums[i] < marker:
                continue
            # if we encounter a point that is exactly as our marker point
            # increment the marker to the next point in range
            if nums[i] == marker:
                marker += 1
                continue
            # otherwise the marker marks the lowest point of
            # range of missing points, so we need to get the range.
            # the high point is possibly marked by the current item in the array
            else:
                high = nums[i]
                # format the string
                string = str(marker) if abs(high-marker) == 1 else "{0}->{1}".format(marker, high-1)
                result.append(string)
                marker = high+1
        # finally, if the marker still hasnt captured the upper point
        # add it.
        if marker <= upper:
            string = str(marker) if upper == marker else "{0}->{1}".format(marker, upper)
            result.append(string)
        return result
