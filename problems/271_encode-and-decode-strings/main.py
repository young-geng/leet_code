# https://leetcode.com/problems/encode-and-decode-strings/
# Algorithm
# Our encode will do this:
# strs = ["hello", "world"]
# strs --> encode --> "5:hello5:world"
# "5:hello5:world" --> decode --> ["hello", "world"]


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        encoded = ''.join("%d:" % len(s) + s for s in strs)
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        decoded = []
        i = 0
        while i < len(s):
            # j will mark the index of columns ":"
            j = s.find(":", i)
            # send the i to next number position
            i = 1 + j + int(s[i:j])
            # extract the substring using j and i
            string = s[j+1: i]
            decoded.append(string)
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
