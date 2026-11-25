class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix.length * matrix[0].length -1;

        while(left<=right){
            int mid = Math.floorDiv(left+right, 2);
            int row = (Math.floorDiv(mid, matrix[0].length));
            int col = (Math.floorMod(mid, matrix[0].length));

            if (target == matrix[row][col]){
                return true;
            }else if(target<matrix[row][col]){
                right--;
            }else if(target>matrix[row][col]){
                left++;
            }
        }
        return false;
    }
}
