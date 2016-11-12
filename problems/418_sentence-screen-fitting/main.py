# https://leetcode.com/problems/sentence-screen-fitting/

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence) + " "
        l = len(s)
        start = 0
        for r in xrange(rows):
            start += cols
            # if we can fit to row without using extra space
            # increment start counter
            if s[start % l] == " ":
                start += 1
            else:
                # we cannot fit perfectly we might need to adjust
                # the new start position
                while start >= 0 and s[(start-1) % l] != " ":
                    start -= 1
        return start/l
