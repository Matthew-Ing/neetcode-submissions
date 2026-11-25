class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> HS = new HashSet<>();

        for(Integer a : nums){
            if (HS.contains(a)){
                return true;
            } else{
                HS.add(a);
            }
        }
        return false;
    }
}