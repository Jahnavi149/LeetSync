/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<>();

        if (root == null){
            return output;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while(q.isEmpty() == false){
            List<Integer> curr_level = new ArrayList<>();
            int levelSize = q.size();
            for (int i=0; i < levelSize; i++){
                TreeNode curr = q.poll();
                curr_level.add(curr.val);

                if (curr.left != null){
                    q.offer(curr.left);
                }
                if(curr.right != null){
                    q.offer(curr.right);
                }
            }
            output.add(curr_level);
        }
        return output;
    }
}