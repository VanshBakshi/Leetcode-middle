class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, current, remaining):
            # Target reached
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                
                # Skip duplicate values at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no later value can work
                if candidates[i] > remaining:
                    break

                # Choose the current number
                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, current, remaining - candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, [], target)

        return result
