class DLL {
    int key;
    int val;
    DLL prev;
    DLL next;

    public DLL (int key, int val){
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
        this.oldest.next = this.latest;
        this.latest.prev = this.oldest;
    }
    // Remove specific node
    private void remove(DLL node){
        DLL prev = node.prev;
        DLL next = node.next;
        prev.next = next;
        next.prev = prev;
    }
    // Add a latest node
    private void add(DLL node){
        DLL prev = latest.prev;
        prev.next = node;
        node.next = latest;
        node.prev = prev;
        latest.prev = node;
    }
    public int get(int key) {
        if(map.containsKey(key)){
            DLL node = map.get(key);
            remove(node);
            add(node);
            return node.getVal();
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            DLL node = map.get(key);
            remove(node);
            DLL newNode = new DLL(key, value);
            add(newNode);
            map.put(key, newNode);
            return;
        }
        if(map.size() == capacity){
            map.remove(oldest.next.getKey());
            remove(oldest.next);   
        }
        DLL newNode = new DLL(key, value);
        add(newNode);
        map.put(key, newNode);  
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */