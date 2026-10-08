class Solution:
    def minCut(self, s):
        n = len(s)

        # dp[i] = minimum cuts needed for s[0:i]
        dp = [i - 1 for i in range(n + 1)]

        # palindrome[i][j] tells whether s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):

                if s[start] == s[end] and (
                    end - start <= 1 or palindrome[start + 1][end - 1]
                ):
                    palindrome[start][end] = True

                    # Whole string s[0:end+1] is palindrome
                    if start == 0:
                        dp[end + 1] = 0
                    else:
                        dp[end + 1] = min(
                            dp[end + 1],
                            dp[start] + 1
                        )

        return dp[n]
