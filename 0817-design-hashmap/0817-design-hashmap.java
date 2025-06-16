class Node {
    int key;
    int val;
    Node next;

    public Node(int key, int val){
        this.key = key;
        this.val = val;
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


class MyHashMap {
    private Node[] arr;

    public MyHashMap() {
        this.arr = new Node[1000];
    }
    
    public void put(int key, int value) {
        int hashKey = key%1000;
        Node node = arr[hashKey]; 
        if(node == null){ arr[hashKey] = new Node(key, value); return; }
        while(node != null){
            if(node.getKey() == key){ node.setVal(value); return; }
            if(node.next == null){ node.next = new Node(key, value); return; }
            node = node.next;
        }     
    }
    
    public int get(int key) {
        int hashKey = key%1000;
        Node node = arr[hashKey];
        while(node != null){
            if (node.getKey() == key){ return node.getVal(); }
            node = node.next;
        }
        return -1;        
    }
    
    public void remove(int key) {
        int hashKey = key%1000;
        Node node = arr[hashKey];
        if(node == null){return;} 
        if (node.getKey() == key){ arr[hashKey] = node.next; return;}
        while(node.next != null){
            if (node.next.getKey() == key) { node.next = node.next.next; return; }
            node = node.next;
        }      
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */