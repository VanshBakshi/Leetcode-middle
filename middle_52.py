class Solution:
    def subsets(self, nums):
        result = []
        current = []

        def backtrack(index):
            result.append(current[:])

            for i in range(index, len(nums)):
                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)

        return result
