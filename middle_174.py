class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        buckets = {}
        size = valueDiff + 1

        for i in range(len(nums)):
            num = nums[i]
            bucket = num // size

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and num - buckets[bucket - 1] <= valueDiff:
                return True

            if bucket + 1 in buckets and buckets[bucket + 1] - num <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // size
                del buckets[old_bucket]

        return False
