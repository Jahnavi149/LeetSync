class DLL {
    int key;
    int val;
    DLL prev;
    DLL next;
    public DLL(int key, int val){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    private int capacity;
    private HashMap<Integer, DLL> map;
    private DLL oldest;
    private DLL latest;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.oldest = new DLL(0, 0);
        this.latest = new DLL(0, 0); 
        this.oldest.next = this.latest;
        this.latest.prev = this.oldest;      
    }

    private void remove(DLL node){
        DLL prev = node.prev;
        DLL next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    private void insert_latest(DLL node){
        DLL prev = latest.prev;
        prev.next = node;
        node.prev = prev;
        node.next = latest;
        latest.prev = node;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            DLL node = map.get(key);
            int value = node.val;
            remove(node);
            insert_latest(node);
            return value;
        }
        return -1;       
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            DLL node = map.get(key);
            node.val = value;
            remove(node);
            insert_latest(node);
            return;
        }
        else{
            if (map.size() == capacity){
                map.remove(oldest.next.key);
                remove(oldest.next);
            }
            DLL new_node = new DLL(key, value);
            map.put(key, new_node);
            insert_latest(new_node);
        }       
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */