class Solution:
    def reverseParentheses(self, s):
        stack = []
        current = []

        for ch in s:
            if ch == '(':
                stack.append(current)
                current = []

            elif ch == ')':
                current.reverse()
                previous = stack.pop()
                previous.extend(current)
                current = previous

            else:
                current.append(ch)

        return ''.join(current)
