# https://leetcode.com/problems/decode-string/

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# Algorithm Explanation
# We keep two stacks one for numbers and other is for chars.
# We walk through the array and if we ever encounter an open parant
# we add an empty string to our char stack. Next time we encounter a char while
# there is still elems in our char stack it means we need to append that char
# to the elem in our front of the stack.
# If we ever encounter a closing parant we need pop from both stacks
# combine the number and string and either add it to the front of our char stack
# or better yet if the stack went empty, we need to add it to the result string
# and continue traversing until we hit the end.


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
                # we already incremented i index so continue
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
