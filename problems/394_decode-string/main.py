# https://leetcode.com/problems/decode-string/

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# Algorithm Explanation

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        numStack = []
        charStack = []
        res = ""
        i = 0
        while i < len(s):
            if ord(s[i]) in xrange(48, 58):
                num = ""
                # consume the digit until it ends.
                while i < len(s) and ord(s[i]) in xrange(48, 58):
                    num += s[i]
                    i += 1
                numStack.append(int(num))
                continue
            elif s[i] == "[":
                charStack.append("")
            elif s[i] == "]":
                num = numStack.pop()
                string = charStack.pop()
                if charStack:
                    parent = charStack.pop()
                    charStack.append(parent + string*num)
                else:
                    res += string*num
            else:
                if charStack:
                    parent = charStack.pop()
                    charStack.append(parent + s[i])
                else:
                    res += s[i]
            i += 1
        return res
