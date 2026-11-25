class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> HM1 = new HashMap<>();
        Map<Character, Integer> HM2 = new HashMap<>();

        for(char a : s.toCharArray()){
            HM1.put(a, HM1.getOrDefault(a, 0)+1);
        } 
        for(char b: t.toCharArray()){
            HM2.put(b, HM2.getOrDefault(b, 0)+1);
        }
        return HM1.equals(HM2);
    }
}
