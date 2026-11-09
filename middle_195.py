import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        n = len(arrival)

        # Count requests handled by each server
        count = [0] * k

        # Segment tree: 1 means available, 0 means busy
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Find first available server >= start
        def find(start):
            def search(node, left, right):
                if right < start or tree[node] == 0:
                    return -1

                if left == right:
                    return left if left < k else -1

                mid = (left + right) // 2

                result = search(node * 2, left, mid)

                if result != -1:
                    return result

                return search(node * 2 + 1, mid + 1, right)

            return search(1, 0, size - 1)

        # Update server availability
        def update(index, value):
            pos = size + index
            tree[pos] = value

            pos //= 2

            while pos:
                tree[pos] = tree[pos * 2] + tree[pos * 2 + 1]
                pos //= 2

        # Min heap: (completion_time, server_id)
        busy = []

        for i in range(n):

            # Release servers whose requests are completed
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            # Find next available server
            server = find(i % k)

            if server == -1:
                server = find(0)

            # Drop request if all servers are busy
            if server == -1:
                continue

            # Assign request
            count[server] += 1

            update(server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find busiest servers
        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]
