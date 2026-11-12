class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> hmap = new HashMap<>();

        for(int a: nums){
            if(hmap.containsKey(a)){
                return true;
            }else{
                hmap.put(a, 1);
            }
        }
        return false;
    }
}