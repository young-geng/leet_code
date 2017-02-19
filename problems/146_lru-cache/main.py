# https://leetcode.com/problems/lru-cache/

# Using a hashtable to keep track of key,value pairs and a doubly linked list
# we can update the cache easily.

class DListNode(object):
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class DList(object):
    """
    DList class
    """
    def __init__(self):
        self.head = DListNode()
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def insertFront(self, node):
        """
        Always add a new node right after the sentinel node.
        """
        if not self.size:
            self.head.next = node
            node.prev = self.head
            self.head.prev = node
            node.next = self.head
        else:
            rest = self.head.next
            rest.prev = node
            node.next = rest
            self.head.next = node
            node.prev = self.head
        self.size += 1

    def insertBack(self, node):
        """
        Inserts a node to the end of the list.
        """
        if self.size == 0:
            self.insertFront(node)
        else:
            before = self.head.prev
            before.next = node
            node.prev = before
            self.head.prev = node
            node.next = self.head
            self.size += 1

    def removeNode(self, node):
        """
        Remove node. Doesn't return anything.
        """
        if not node:
            return
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def popTail(self):
        """
        Remove the tail node and return it.
        Returns None if list is empty.
        """
        if self.size == 0:
            return
        back = self.head.prev
        self.removeNode(back)
        return back

    def moveToHead(self, node):
        """
        Removes node and puts it to the front of the list.
        """
        self.removeNode(node)
        self.insertFront(node)

    # getter for head
    def head(self):
        """
        Returns the head of the list. If the list is empty returns None.
        This node is strictly the node right after the sentinel which head
        points to.
        """
        if not self.size:
            return
        return self.head.next

    def tail(self):
        """
        Returns the tail of list. If the list is empty returns None.
        This node is the node that comes right before sentinel which head
        variable points to.
        """
        if not self.size:
            return None
        return self.head.prev

class LRUCache(object):
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.dlist = DList()
        self.dictionary = {} # <key, value=DListNode>

    def get(self, key):
        """
        Use the hashtable to get the node in O(1) time.
        If key doesn't exists then return -1.
        If it does than move the node to the front of the DList.

        Return:
        node value
        """
        node = self.dictionary.get(key, None)
        if not node:
            return -1
        # node is accessed so move it to head of dlist
        self.dlist.moveToHead(node)
        return node.val

    def put(self, key, value):
        # if key exists, update its value
        node = self.dictionary.get(key, None)
        if node:
            node.val = value
            self.dlist.moveToHead(node)
        else:
            # node doesnt exists
            node =  DListNode(key, value)
            # now if cap is reached, remove the last entry
            if self.count >= self.capacity:
                eldest = self.dlist.popTail()
                del self.dictionary[eldest.key]
                self.count -= 1

            self.dictionary[key] = node
            self.dlist.insertFront(node)
            self.count += 1
