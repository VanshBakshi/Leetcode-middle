class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True

            seen[nums[i]] = i

        return False
