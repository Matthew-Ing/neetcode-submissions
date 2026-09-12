class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        to = []

        for a in tokens:

            try:
                to.append(int(a))

            except:
                to.append(a)
            
            if to[-1] == "+":
                to.pop()
                num = to[-2] + to[-1]
                to.pop()
                to.pop()
                to.append(num)
                print(to[-1])
            if to[-1] == "-":
                to.pop()
                num = to[-2] - to[-1]
                to.pop()
                to.pop()
                to.append(num)
                print(to[-1])
            if to[-1] == "*":
                to.pop()
                num = to[-2] * to[-1]
                to.pop()
                to.pop()
                to.append(num)
                print(to[-1])
            if to[-1] == "/":
                to.pop()
                num = to[-2] / to[-1]
                to.pop()
                to.pop()
                to.append(int(num))
                print(to[-1])
        return to[-1]