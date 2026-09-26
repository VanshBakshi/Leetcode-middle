class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            # Target reached
            if total == target:
                result.append(current[:])
                return

            # Sum exceeded
            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Since candidates are positive
                if total + num > target:
                    continue

                # Choose
                current.append(num)

                # We use i again because the same number
                # can be selected unlimited times
                backtrack(i, current, total + num)

                # Undo choice
                current.pop()

        backtrack(0, [], 0)

        return result
