class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]
