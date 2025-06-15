class DLL{
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

class LRUCache{
    private int capacity;
    private HashMap<Integer, DLL> map;
    private DLL oldest, latest;
    
    public LRUCache(int capacity){
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.oldest = new DLL(0, 0);
        this.latest = new DLL(0, 0);
        oldest.next = latest;
        latest.prev = oldest;
    }
    // Insert as latest
    private void insert(DLL node){
        DLL prev = latest.prev;
        prev.next = node;
        node.prev = prev;
        node.next = latest;
        latest.prev = node;
    }
    //Remove node
    private void remove(DLL node){
        DLL prev = node.prev;
        DLL next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    public int get(int key){
        if(map.containsKey(key)){
            DLL node = map.get(key);
            remove(node);
            insert(node);
            return node.val;
        }
        return -1;
    }
    public void put(int key, int val){
        if(map.containsKey(key)){
            DLL node = map.get(key);
            map.remove(key);
            remove(node);
            DLL new_node = new DLL(key, val);
            insert(new_node);
            map.put(key, new_node);
        }
        else{
            if(map.size() == capacity){
                DLL node = oldest.next;
                oldest.next = oldest.next.next;
                oldest.next.prev = oldest;
                map.remove(node.key);
            }
            DLL new_node = new DLL(key, val);
            map.put(key, new_node);
            insert(new_node);
        }
    }
}
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */