class Solution:
    def combine(self, n, k):
        result = []
        current = []

        def backtrack(start):
            if len(current) == k:
                result.append(current[:])
                return

            for num in range(start, n + 1):
                current.append(num)

                backtrack(num + 1)

                current.pop()

        backtrack(1)

        return result
