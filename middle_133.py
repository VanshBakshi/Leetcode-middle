class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        clones = {}

        def dfs(original):
            # Already cloned
            if original in clones:
                return clones[original]

            # Create clone
            copy = Node(original.val)
            clones[original] = copy

            # Clone all neighbors
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
