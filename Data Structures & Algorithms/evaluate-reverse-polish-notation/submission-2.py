class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = {"+","-","*","/"}
        for token in tokens:
            if token not in s:
                stack.append(int(token))
                continue
            n2 = stack.pop()
            n1 = stack.pop()
            if token == "+":
                stack.append(n1 + n2)
            elif token == "-":
                stack.append(n1 - n2)
            elif token == "*":
                stack.append(n1 * n2)
            elif token == "/":
                stack.append(int(n1 / n2))
            
        return stack[0]