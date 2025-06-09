class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [None]*1000
        
    def put(self, key: int, value: int) -> None:
        hash_key = key%1000
        if self.hashmap[hash_key] is None:
            self.hashmap[hash_key] = Node(key, value)
            return
        else:
            node = self.hashmap[hash_key]
            while node:
                if node.key == key:
                    node.val = value
                    return
                if node.next is None:
                    break
                node = node.next
            node.next = Node(key, value)

        
    def get(self, key: int) -> int:
        hash_key = key%1000
        node = self.hashmap[hash_key]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
        
    def remove(self, key: int) -> None:
        hash_key = key%1000
        node = self.hashmap[hash_key]
        if node is None:
            return
        if node.key == key:
            self.hashmap[hash_key] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)