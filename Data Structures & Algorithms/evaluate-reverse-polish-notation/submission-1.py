class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = {"+","-","*","/"}
        for token in tokens:
            if token not in s:
                stack.append(token)
                continue
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            if token == "+":
                stack.append(n1 + n2)
            elif token == "-":
                stack.append(n1 - n2)
            elif token == "*":
                stack.append(n1 * n2)
            elif token == "/":
                stack.append(n1 / n2)
            
        return int(stack[0])