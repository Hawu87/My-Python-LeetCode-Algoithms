# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()       
        list1, list2, carry = l1, l2, 0
        while list1 or list2 or carry:
            one = list1.val if list1 else 0
            two = list2.val if list2 else 0
            total = one + two + carry

            value = total % 10
            carry = total // 10
            tail.next = ListNode(value)
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            tail = tail.next

        return dummy.next
