class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String a : tokens){
            if (a.equals("+")){
                int b = stack.pop();
                int c = stack.pop();
                stack.push(b+c);
            }else if (a.equals("-")){
                int b = stack.pop();
                int c = stack.pop();
                stack.push(c-b);
            } else if (a.equals("*")){
                int b = stack.pop();
                int c = stack.pop();
                stack.push(b*c);
            }else if (a.equals("/")){
                int b = stack.pop();
                int c = stack.pop();
                stack.push(c/b);
            }else{
                stack.push(Integer.parseInt(a));
            }
        }
        return stack.peek();
    }
}
