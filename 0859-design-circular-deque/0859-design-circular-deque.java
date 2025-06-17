class MyCircularDeque {
    private int k;
    private int[] dq;
    private int front;
    private int rear;

    public MyCircularDeque(int k) {
        this.k = k;
        this.dq = new int[k];
        this.front = -1;
        this.rear = -1;      
    }
    
    public boolean insertFront(int value) {
        if(isFull()){ return false; }
        if(isEmpty()){ front = 0; rear = 0; dq[front] = value; return true; }
        front = (front-1+k)%k;
        dq[front] = value;
        return true;
    }
    
    public boolean insertLast(int value) {
        if(isFull()){ return false; }
        if(isEmpty()){ front = 0; rear = 0; dq[rear] = value; return true; }
        rear = (rear+1)%k;
        dq[rear] = value;
        return true;
    }
    
    public boolean deleteFront() {
        if(isEmpty()){ return false; }
        if(front == rear){ dq[front] = -1; front = -1; rear = -1; return true; }
        dq[front] = -1;
        front = (front+1)%k;
        return true;  
    }
    
    public boolean deleteLast() {
        if(isEmpty()){ return false; }
        if(front == rear){ dq[rear] = -1; front = -1; rear = -1; return true; }
        dq[rear] = -1;
        rear = (rear-1+k)%k;
        return true; 
    }
    
    public int getFront() {
        if(isEmpty()){ return -1; }
        return dq[front];
    }
    
    public int getRear() {
        if(isEmpty()){ return -1; }
        return dq[rear];
    }
    
    public boolean isEmpty() {
        return front == -1;  
    }
    
    public boolean isFull() {
        return (front - 1+k)%k == rear;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */