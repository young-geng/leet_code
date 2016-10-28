# https://leetcode.com/problems/minimum-window-substring/
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = 0
        charToCount = dict.fromkeys(t, 0)
        substring = ""
        minsofar = float('inf')
        tail = 0
        for head in xrange(len(s)):
            # if we dont yet have a valid substring, keep moving
            if s[head] in charToCount:
                if charToCount[s[head]] == 0:
                    count += 1
                charToCount[s[head]] += 1

            # if we have a valid substring
            while count == len(charToCount):
                # check if its better than current minimum
                if len(s[tail:head+1]) < minsofar:
                    substring = s[tail:head+1]
                    minsofar = len(s[tail:head+1])
                # stop h increment t until you break the validity
                # in this case, until count drops
                if s[tail] in charToCount:
                    charToCount[s[tail]] -= 1
                    if charToCount[s[tail]] == 0:
                        count -= 1
                tail += 1
        return substring
