class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s;
        chars = list(s)
        # Two pointer method
        i, j = 0, len(chars)-1
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return "".join(chars)
