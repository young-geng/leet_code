class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.nxt = {}
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
            if c not in curr.nxt:
                curr.nxt[c] = TrieNode(c)
            curr = curr.nxt[c]
        curr.word = word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr.nxt:
                return False
            curr = curr.nxt[c]
        return curr.word != ''


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr.nxt:
                return False
            curr = curr.nxt[c]
        return curr.word != '' or len(curr.nxt) > 0


if __name__ == "__main__":
# Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
