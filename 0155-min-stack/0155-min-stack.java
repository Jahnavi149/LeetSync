class MinStack {
    Stack<Integer> regSt;
    Stack<Integer> minSt;

    public MinStack() {
       this.regSt = new Stack<>();
       this.minSt = new Stack<>();
    }
    
    public void push(int val) {
        regSt.push(val);
        if(minSt.isEmpty()){ minSt.push(val); }
        else { minSt.push(Math.min(val, minSt.peek())); }
        
    }
    
    public void pop() {
        minSt.pop();
        regSt.pop();
    }
    
    public int top() {
        return regSt.peek(); 
    }
    
    public int getMin() {
        return minSt.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */