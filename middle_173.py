class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                if i == size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
