class MyHashMap:

    def __init__(self):
        self.array = [-1]*(pow(10, 6)+1)
        self.present = [False]*(pow(10, 6)+1)
        
    def put(self, key: int, value: int) -> None:
        self.array[key] = value
        self.present[key] = True       

    def get(self, key: int) -> int:
        return self.array[key]
        
    def remove(self, key: int) -> None:
        self.array[key] = -1
        self.present[key] = False
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)