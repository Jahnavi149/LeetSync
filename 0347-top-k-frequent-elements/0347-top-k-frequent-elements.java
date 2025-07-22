class Freq {
    int ele, freq;

    public Freq(int ele, int freq){
        this.ele = ele;
        this.freq = freq;
    }

    public int getFreq(){
        return freq;
    }

    public int getEle(){
        return ele;
    }
}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for(int n : nums){
            if(freq.containsKey(n)){
                freq.put(n, freq.get(n)+1);
            }
            else{
                freq.put(n, 1);
            }
        }
        PriorityQueue<Freq> min_heap = new PriorityQueue<>((a, b) -> a.getFreq() - b.getFreq());

        freq.forEach((Integer a, Integer b) -> {
            Freq obj = new Freq(a, b);
            min_heap.add(obj);
            if(min_heap.size() > k){ min_heap.poll(); }
        });

        int[] output = new int[k];
        for(int i=0; i<k; i++){
            output[i] = min_heap.poll().getEle();
        }
        return output;
    }
}