class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> hMap = new HashMap<>();
        hMap.put(')', '(');
        hMap.put('}', '{');
        hMap.put(']', '[');
        Stack<Character> stack = new Stack<>();

        for(char a: s.toCharArray()){
            if(hMap.containsKey(a)){
                if (!stack.isEmpty() && stack.peek() == hMap.get(a)){
                stack.pop();
                } else{
                    return false;
                }
            }
            if(hMap.containsValue(a)){
                stack.push(a);
            }
        }
        if (stack.isEmpty()){
            return true;
        }else{
            return false;
        }
    }
}
