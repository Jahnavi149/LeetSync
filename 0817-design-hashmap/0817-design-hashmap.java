class LL {
    int key;
    int val;
    LL next;
    public LL(int key, int val){
        this.key = key;
        this.val = val;
    }

    public int getKey(){ return key; }
    public int getVal(){ return val; }
    public void setVal(int value){ val = value; }
}

class MyHashMap {
    LL[] map;
    int mod = 1000;

    public MyHashMap() {
        this.map = new LL[mod];
        for(int i=0; i<mod; i++){
            map[i] = null;
        }
    }
    
    public void put(int key, int value) {
        int key_mod = key%mod;
        LL node = map[key_mod];
        if(node == null){
            map[key_mod] = new LL(key, value);
            return;
        }
        while(node.next != null && node.getKey() != key){
            node = node.next;
        }
        if(node.getKey() == key){ node.setVal(value); return; }
        node.next = new LL(key, value);    
    }
    
    public int get(int key) {
        int key_mod = key%mod;
        LL node = map[key_mod];
        if(node == null){
            return -1;
        }
        while(node != null){
            if(node.getKey() == key){
                return node.getVal();
            }
            node = node.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int key_mod = key%mod;
        LL node = map[key_mod];
        if(node == null){
            return;
        }
        if(node.getKey() == key){
            map[key_mod] = node.next; return;
        }
        while(node.next != null && node.next.getKey() != key){
            node = node.next;
        }
        if(node.next == null){ return; }
        node.next = node.next.next;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */