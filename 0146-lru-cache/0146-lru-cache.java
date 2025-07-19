class DLL {
    int key;
    int val;
    DLL prev, next;

    public DLL(int key, int val){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }

    public int getKey(){
        return key;
    }

    public int getVal(){
        return val;
    }

    public void setVal(int value){
        val = value;
    }
}

class LRUCache {
    int capacity;
    HashMap<Integer, DLL> map;
    DLL oldest, latest;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.oldest = new DLL(0, 0);
        this.latest = new DLL(0, 0);
        latest.next = oldest;
        oldest.prev = latest;  
    }

    public void remove(DLL node){
        DLL prev = node.prev, next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    public void addLatest(DLL node){
        DLL next = latest.next;
        latest.next = node;
        node.prev = latest;
        node.next = next;
        next.prev = node;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            DLL node = map.get(key);
            int val = node.getVal();
            remove(node);
            addLatest(node);
            return val;
        }
        return -1;  
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            DLL node = map.get(key);
            node.setVal(value);
            map.put(key, node);
            remove(node);
            addLatest(node);
            return;
        }
        if(map.size() == capacity){
            DLL lru = oldest.prev;
            int lru_key = lru.getKey();
            map.remove(lru_key);
            remove(lru);
        }
        DLL newNode = new DLL(key, value);
        map.put(key, newNode);
        addLatest(newNode);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */