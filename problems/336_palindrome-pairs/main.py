# https://leetcode.com/problems/palindrome-pairs/
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        words_dict = {}
        out = []
        for i in xrange(len(words)):
            words_dict[words[i]] = i

        for i in xrange(len(words)):
            word = words[i]
            for j in xrange(len(word)+1):
                left = word[:j]
                right = word[j:]
                left_i = words_dict.get(left[::-1], None)
                if left_i and left_i != i and self.is_palindrome(right):
                    out.append([i,left_i])

                right_i = words_dict.get(right[::-1], None)
                if right_i and right_i != i and self.is_palindrome(left):
                    out.append([right_i, i])

        return out

    def is_palindrome(self, string):
        """
        Given a string returns T/F is string is palindrome.
        """
        i,j = 0, len(string)-1
        while i <= j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
