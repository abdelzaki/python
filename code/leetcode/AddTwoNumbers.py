"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list."""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        start = prev = ListNode(0)
        rest = 0
        while l1 or l2 or rest:
            # calculate value
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + rest
            node = ListNode(val % 10)
            rest = int(val / 10)
            prev.next = node
            prev = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        head = start.next
        while head:
            print(head.val)
            head = head.next


c1_3, c2_3 = ListNode(4), ListNode(4)
c1_2, c2_2 = ListNode(4), ListNode(4, c2_3)
c1_1, c2_1 = ListNode(2, c1_2), ListNode(3, c2_2)
#c1_0, c2_0 = ListNode(9, c1_1), ListNode(9, c2_1)
c1_0, c2_0 = ListNode(0), ListNode(1)
Solution.addTwoNumbers(c1_0, c2_0)
solution = Solution()
