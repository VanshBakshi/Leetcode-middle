class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(s, open_count, close_count):
            # Complete valid combination
            if len(s) == 2 * n:
                result.append(s)
                return

            # Add opening parenthesis
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add closing parenthesis
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result
