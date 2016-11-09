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
    def __init__(self):
        self.head = DListNode()
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def insertFront(self, node):
        """
        Always a add a new node right after the sentinel node.
        This newly added node becomes the new head.
        """
        if self.size == 0:
            self.head.next = front
            node.prev = head
            self.head.prev = front
            node.next = self.head
        else:
            rest = self.head.next
            rest.prev = node
            node.next = rest
            self.head.next = node
            node.prev = self.head
        self.size += 1

    def insertBack(self, node):
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
        if not node:
            return
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def popTail(self):
        # pop tail and return
        if self.size == 0:
            return
        back = self.head.prev
        self.removeNode(back)
        return back

    def moveToHead(self, node):
        # move a node to head of DList
        self.removeNode(node)
        self.insertFront(node)


class LRUCache(object):
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.dlist = DList()
        self.cache = {} # <key, value=DListNode>

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        # node is accessed so move it to head of dlist
        self.dlist.moveToHead(node)
        return node.val

    def set(self, key, val):
        # if a key exists, update the value
        # if not add to front of cache
        node = self.cache.get(key, None)
        if node:
            node.val = val
            # move to cache head
            self.dlist.moveToHead(node)
        else:
            # node doesnt exist, put it to cache checking the capacity
            node = DListNode(key=key,val=val)
            self.cache[key] = node
            self.dlist.insertFront(node)
            self.count += 1
            # capacity breached, invalidate the tail in cache
            if self.count > self.capacity:
                # remove tail from cache dlist
                tail = self.dlist.popTail()
                # remove tail from hashtable
                del self.cache[tail.key]
                self.count -= 1    
