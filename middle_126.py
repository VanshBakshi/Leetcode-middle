from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)
        queue = deque([beginWord])
        visited = set([beginWord])

        found = False

        while queue and not found:
            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        new_word = word[:i] + c + word[i + 1:]

                        if new_word not in words:
                            continue

                        if new_word not in visited:
                            if new_word not in level_visited:
                                level_visited.add(new_word)
                                queue.append(new_word)

                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

            visited.update(level_visited)

        if endWord not in parents:
            return []

        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result
