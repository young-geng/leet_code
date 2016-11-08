# https://leetcode.com/problems/word-break/

# this is a DP question and the way I solved was the following
# you are going to keep a list that represents the indices you can
# segment this string, because you can segment it in final index,
# the array length will be +1 of string len
# you are going to keep two pointers i will move infront, j will try to
# catch up to i.
# the DP update formula is as follows
# at index segmentable[i] you can either segment it at that point or not
# if you can segment it at there it means the substring s[j:i] must
# be in the dictionary and that you were able segment in jth position,
# segmentable[j] == True
# if not then you move j until it reaches i
# if you still havent segment it move on to next char using i
# at the end you need to return segmentable last elem cuz we are
# asked if its able to segment the whole string.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return False

        segmentable = [False]*(len(s)+1)
        segmentable[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                substring = s[j:i]
                if segmentable[j] and substring in wordDict:
                    segmentable[i] = True
                    break
        return segmentable[len(s)]
