# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []

        for i in xrange(len(s)):
            # if its opening it, its getting deeper so add to stack
            if s[i] in "([{":
                stack.append(s[i])
            # if not it must be a closing parenth
            # in which case check if stack is empty if not pop and check
            # whether popped elem is closed with the current item
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if s[i] == ")" and last != "(": return False
                if s[i] == "]" and last != "[": return False
                if s[i] == "}" and last != "{": return False
        return len(stack) == 0
