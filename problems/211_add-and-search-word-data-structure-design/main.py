# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.word = ''


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = TrieNode(c)
            curr = curr.next[c]
        curr.word = word

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain
        the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._backtracking_search(word, 0, self.root)

    def _backtracking_search(self, word, idx, parent):
        # if reached the end of word
        if idx == len(word):
            # node should contain word field filled by addWord,
            # it shouldn't be empty.
            return parent.word != ''

        c = word[idx]
        if c == '.':
            # search every branch
            children = parent.next.values()
            for child in children:
                b = self._backtracking_search(word, idx+1, child)
                if b:
                    return True
            return False
        # else search normally
        if c not in parent.next:
            return False
        child = parent.next[c]
        return self._backtracking_search(word, idx+1, child)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
