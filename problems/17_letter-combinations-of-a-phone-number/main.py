# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # empty input check
        if len(digits) == 0:
            return []
        combinations = [""]
        phone_keys = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for digit in list(digits):
             temp = []
             chars = phone_keys[int(digit)]
             for char in chars:
                 for i in xrange(len(combinations)):
                     temp.append(combinations[i] + char)
             combinations = temp
        return combinations
