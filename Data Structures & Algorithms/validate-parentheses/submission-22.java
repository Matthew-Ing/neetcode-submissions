class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> brackets = new HashMap<>();

        brackets.put('}', '{');
        brackets.put(')', '(');
        brackets.put(']', '[');

        for (char a : s.toCharArray()){
            if (brackets.containsValue(a)){
                stack.push(a);
                System.out.println("stack pushed");
            }else if (!stack.isEmpty() && brackets.get(a) == stack.peek()){
                stack.pop();
                System.out.println("stack popped");
            }else{
                System.out.println("stack returned");
                return false;
            }
        }
        return stack.isEmpty();
    }
}
