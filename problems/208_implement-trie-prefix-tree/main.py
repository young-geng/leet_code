class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.word = ''

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = TrieNode(c)
            curr = curr.next[c]
        # leaf node has word field storing the entire word.
        curr.word = word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        # curr node must have the word field filled from insertion.
        return curr.word != ''


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        return True
        # to be more rigorous
        # return curr.word != '' or len(curr.next) > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
