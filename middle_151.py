class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    for rest in dfs(end):
                        if rest:
                            result.append(word + " " + rest)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return dfs(0)
