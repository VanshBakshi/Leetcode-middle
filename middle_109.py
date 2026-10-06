class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            # Leaf node
            if node.left is None and node.right is None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))
