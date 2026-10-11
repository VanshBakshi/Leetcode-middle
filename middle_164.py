class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    result = abs(a) // abs(b)
                    if (a < 0) != (b < 0):
                        result = -result
                    stack.append(result)

        return stack[-1]
