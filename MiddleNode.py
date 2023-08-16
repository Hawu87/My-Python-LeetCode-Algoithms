# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    length = getLength(linkedList)
    mid = length // 2
    temp = linkedList
    for _ in range(mid):
        temp = temp.next
    return temp

def getLength(linkedList):
    count = 0
    temp = linkedList
    while temp:
        count += 1
        temp = temp.next
    return count

def middleNode2(linkedList):
    slow = fast = linkedList
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
