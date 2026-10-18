class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node['#'] = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return '#' in node

            ch = word[i]

            if ch == '.':
                for key in node:
                    if key != '#' and dfs(node[key], i + 1):
                        return True
                return False

            if ch not in node:
                return False

            return dfs(node[ch], i + 1)

        return dfs(self.root, 0)
