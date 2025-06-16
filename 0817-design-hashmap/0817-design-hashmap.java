class Node {
    int key;
    int val;
    Node next;

    public Node(int key, int val){
        this.key = key;
        this.val = val;
        this.next = null;
    }
}

class MyHashMap {
    Node[] arr;

    public MyHashMap() {
        this.arr = new Node[1000];
        
    }
    
    public void put(int key, int value) {
        int hashCode = key%1000;
        Node node = arr[hashCode];
        if(node == null){ arr[hashCode] = new Node(key, value); return; }
        while(node != null){
            if(node.key == key){ node.val = value; return; }
            if(node.next == null){ node.next = new Node(key, value); }
            node = node.next;
        }    
    }
    
    public int get(int key) {
        int hashCode = key%1000;
        Node node = arr[hashCode];
        while(node != null){
            if(node.key == key){ return node.val; }
            node = node.next;
        }
        return -1;   
    }
    
    public void remove(int key) {
        int hashCode = key%1000;
        Node node = arr[hashCode];
        if(node == null){ return; }
        if(node.key == key){ arr[hashCode] = node.next; return; }
        while(node.next != null){
            if(node.next.key == key){ node.next = node.next.next; return;}
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