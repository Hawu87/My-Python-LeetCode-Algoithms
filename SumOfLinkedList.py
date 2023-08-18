# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    dummy = tail = LinkedList(None)
    carry = 0
    temp1, temp2 = linkedListOne, linkedListTwo
    while temp1 or temp2:
        val1 = temp1.value if temp1 else 0
        val2 = temp2.value if temp2 else 0
        total = val1 + val2 + carry

        val = total % 10
        new_node = LinkedList(val)
        tail.next = new_node
        tail = tail.next

        carry = total // 10
        temp1 = temp1.next if temp1 else None
        temp2 = temp2.next if temp2 else None

    if carry > 0:
        tail.next = LinkedList(carry)
    return dummy.next
        
        
