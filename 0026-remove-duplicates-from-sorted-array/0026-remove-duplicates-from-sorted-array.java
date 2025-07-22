class Solution {
    public int removeDuplicates(int[] nums) {
        int currEle = nums[0];
        int i = 1;
        int count = 1;
        while(i < nums.length){
            if(nums[i] != currEle){
                nums[count++] = nums[i];
                currEle = nums[i];
            }
            i++;
        }
        return count;
    }
}