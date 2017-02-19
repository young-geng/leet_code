# https://leetcode.com/problems/reverse-vowels-of-a-string/

"""
Two pointer technique. Start i from the beginning and j from the end.
* Increment i until it hits a vowel.
* Decrement j until it hits a vowel.
* Swap vowels in i and j.
* increment i and decrement j.
Do this while i < j.

Runtime: O(N)
Space: O(N)
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        i, j = 0, len(s)-1
        chars = list(s)
        while i < j:
            while i < j and chars[i] not in vowels:
                i += 1

            while i < j and chars[j] not in vowels:
                j -= 1

            # swap the vowels.
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        return "".join(chars)
