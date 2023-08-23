# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
    """my_hash = set()
        temp = head
        while temp:
            if temp in my_hash:
                return True
            my_hash.add(temp)
            temp = temp.next
        return False
    """
