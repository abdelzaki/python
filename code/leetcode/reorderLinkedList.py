"""You are given the head of a singly linked-list. The list can be represented as:"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        arrayLinkedList = list()
        current = head
        while current:
            arrayLinkedList.append(current)
            current = current.next
        l = 1
        r = len(arrayLinkedList) 
        if r < 2:
            return head
        current = head
        while l <= r:
            r -= 1
            current.next = arrayLinkedList[r]
            current = current.next
            current.next = arrayLinkedList[l]
            prev = current
            current = current.next
            l += 1
        prev.next = None
        node = head
        while node:
            print(node.val)
            node = node.next
c6 = ListNode(6, None)
c5 = ListNode(5, c6)
c4 = ListNode(4, c5)
c3 = ListNode(3, c4)
c2 = ListNode(2, c3)
c1 = ListNode(1, None)

sol = Solution()
sol.reorderList(c1)