class Solution:
    def maxPathSum(self, root):
        self.answer = -1000000000

        def dfs(node):
            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current = node.val + left + right

            self.answer = max(self.answer, current)

            return node.val + max(left, right)

        dfs(root)
        return self.answer
