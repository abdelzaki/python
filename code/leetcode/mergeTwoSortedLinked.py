
"""Merge Two Sorted Lists"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


c1_2, c2_2 = ListNode(4), ListNode(4)
c1_1, c2_1 = ListNode(2, c1_2), ListNode(3, c2_2)
c1_0, c2_0 = ListNode(1, c1_1), ListNode(1, c2_1)


class Solution:
    def __init__(self) -> None:
        pass

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        c1, c2 = list1, list2
        dummy = ListNode()
        current = dummy
        while c1 and c2:
            if c1.val < c2.val:
                current.next = c1
                c1 = c1.next
            else:
                current.next = c2
                c2 = c2.next
            current = current.next
        current.next = c1 if c1 else c2
        return dummy.next


s = Solution()
s.mergeTwoLists(c1_0, c2_0)
