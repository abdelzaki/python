"""Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    """Using fast and slow pointer which start from the head """
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    def hasCycleWithMap(self, head: ListNode) -> bool:
        unique = set()
        while head:
            if head in unique:
                return True
            unique.add(head)
            head = head.next
        return False
            

c6 = ListNode(6, None)
c5 = ListNode(5, c6)
c4 = ListNode(4, c5)
c3 = ListNode(3, c4)
c2 = ListNode(2, c3)
c1 = ListNode(1, c2)
c6.next = None
solution = Solution()
print(solution.hasCycleWithMap(c1))
