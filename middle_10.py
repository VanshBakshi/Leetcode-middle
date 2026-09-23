class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        # x is greater than total sum
        if target < 0:
            return -1

        # Need to remove all elements
        if target == 0:
            return len(nums)

        left = 0
        current_sum = 0
        max_len = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink the window
            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            # Found a subarray with required sum
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len
