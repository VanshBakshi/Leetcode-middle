class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[j] means:
        # using first i characters of s1
        # and first j characters of s2
        # can we form first i+j characters of s3?
        dp = [False] * (len(s2) + 1)

        dp[0] = True

        # Using only s2
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            # Using only s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len(s2) + 1):

                # Take character from s1
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]

                # Take character from s2
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[j] = from_s1 or from_s2

        return dp[len(s2)]
