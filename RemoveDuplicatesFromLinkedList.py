# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    curr = linkedList
    while curr is not None:
        nextDist = curr.next
        while nextDist is not None and curr.value == nextDist.value:
            nextDist = nextDist.next
        curr.next = nextDist
        curr = nextDist
    return linkedList
