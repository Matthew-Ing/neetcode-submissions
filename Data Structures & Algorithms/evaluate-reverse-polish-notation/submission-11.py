class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for a in tokens:
            if a == "+":
                stack.append(stack.pop()+stack.pop())
            elif a == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif a == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            elif a == "*":
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(a))
            # print(a, stack)
        return stack[0]