class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> HM = new HashMap<>();

        for(int i = 0; i<=nums.length;i++){
            int a = nums[i];
            int b = target - a;
            if (HM.containsKey(b)){
                return(new int[]{HM.get(b), i});
            }else{
                HM.put(a, i);
            }
        }
        return new int[]{};
    }
}
