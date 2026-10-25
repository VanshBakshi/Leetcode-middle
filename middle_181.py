class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    top = stack.pop()
                    result = abs(top) // num
                    if top < 0:
                        result = -result
                    stack.append(result)

                sign = ch
                num = 0

        return sum(stack)
