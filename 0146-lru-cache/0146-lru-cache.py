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

    # Insert as the latest 
    def _insert(self, node):
        prev = self.latest.prev
        prev.next = node
        node.prev = prev
        node.next = self.latest
        self.latest.prev = node

    # Remove given node
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
        if key in self.cache:
            node = self.cache[key]
            del self.cache[key]
            self._remove(node)

        if len(self.cache) == self.capacity:
            oldest = self.oldest.next
            del self.cache[oldest.key]
            self._remove(oldest)

        new_node = Node(key, value)
        self._insert(new_node)
        self.cache[key] = new_node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)