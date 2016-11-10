# https://leetcode.com/problems/reverse-words-in-a-string-ii/

# Algorithm:
# 1) reverse the individual words in char array delimited by " " char.
# 2) reverse the entire string and return

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def reverseRange(i, j):
            while 0 <= i < j < len(s):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        start = 0
        s.append(" ")
        for i,c in enumerate(s):
            if c == " ":
                reverseRange(start, i-1)
                start = i + 1
        s.pop()
        reverseRange(0, len(s)-1)
