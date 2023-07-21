class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "-":
                l, r = stack.pop(), stack.pop()
                stack.append(r - l)
            elif i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                l, r = stack.pop(), stack.pop()
                stack.append(int(r / l))
            else:
                stack.append(int(i))
        return stack[0]
