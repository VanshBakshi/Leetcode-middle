class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev = 0
            curr = 0

            for money in houses:
                prev, curr = curr, max(curr, prev + money)

            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
