# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        charToCount = {}
        # max_index keeps the maximum count of a char,
        # to decide on later array size
        max_index = 0
        for char in s:
            # if char doesn't exist in dict, add it to dict.
            if charToCount.get(char, None) == None:
                charToCount[char] = 1
            else:
                charToCount[char] += 1
            max_index = max(max_index, charToCount[char])

        frequencies = [-1]*(max_index+1)
        for char in charToCount:
            # charToCount[char] --> (int) which is index in array.
            i = charToCount[char]
            if frequencies[i] == -1:
                frequencies[i] = [char]
            else:
                frequencies[i].append(char)
        return self.recoverString(frequencies)

    def recoverString(self, arr):
        """ recovers a string using arr as a frequencies array."""
        out = ""
        for i in xrange(len(arr)-1, -1, -1):
            if arr[i] != -1:
                for s in map(lambda c: c*i, arr[i]):
                    out += s
        return out
