class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        res = 0

        for a in tokens:
            if a == "+":
                b = stack.pop()
                c= stack.pop()
                stack.append(b+c)
            elif a == "-":
                b = stack.pop()
                c= stack.pop()
                stack.append(c-b)

            elif a == "*":
                b = stack.pop()
                c= stack.pop()
                stack.append(b*c)
            elif a == "/":
                b = stack.pop()
                c= stack.pop()
                stack.append(int(c/b))
            else:
                stack.append(int(a))

        return stack[-1]