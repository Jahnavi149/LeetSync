class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
    
    # Inserting at the end 
    def _insert(self, node):
        prev = self.latest.prev
        prev.next = node
        node.next = self.latest
        node.prev = prev
        self.latest.prev = node

    # Remove node from dll
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                del self.cache[self.oldest.next.key]
                self._remove(self.oldest.next)
        else:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
"""        
cap = 2
put(1,1) : 1 -> Node(1), Node(0) -> Node(1) -> Node(0)
put(2,2) : 2 -> Node(2), Node(0) -> Node(1) -> Node(2) -> Node(0)
get(1) : Node(0) -> Node(2) -> Node(1) -> Node(0)
put(3,3) : 3 -> Node(3), Node(0) -> Node(1) -> Node(0), Node(0) -> Node(1) -> Node(3) -> Node(0)
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)