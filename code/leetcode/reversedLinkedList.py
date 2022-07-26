"""Given the head of a singly linked list, reverse the list, and return the reversed list."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


c6 = ListNode(6)
c5 = ListNode(5, c6)
c4 = ListNode(4, c5)
c3 = ListNode(3, c4)
c2 = ListNode(2, c3)
c1 = ListNode(1, c2)

solution = Solution()
head = solution.reverseList(c1)
while head:
    print(head.val)
    head = head.next
